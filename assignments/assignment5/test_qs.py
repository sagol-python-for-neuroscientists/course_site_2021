import pathlib

import pytest

from hw5 import *


def test_valid_input():
    fname = pathlib.Path(__file__)
    q = QuestionnaireAnalysis(fname)
    assert fname == q.data_fname


def test_str_input():
    q = QuestionnaireAnalysis(__file__)
    assert pathlib.Path(__file__) == q.data_fname


def test_missing_file():
    fname = pathlib.Path('teststs.fdfd')
    with pytest.raises(ValueError):
        QuestionnaireAnalysis(fname)


def test_wrong_input_type():
    fname = 2
    with pytest.raises(TypeError):
        q = QuestionnaireAnalysis(pathlib.Path(fname))


def test_data_attr_exists():
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    assert hasattr(q, 'data')


def test_data_attr_is_df():
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    assert isinstance(q.data, pd.DataFrame)


def test_correct_age_distrib_hist():
    truth = np.load('tests_data/q1_hist.npz')
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    assert np.array_equal(q.show_age_distrib()[0], truth['hist'])


def test_correct_age_distrib_edges():
    truth = np.load('tests_data/q1_hist.npz')
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    assert np.array_equal(q.show_age_distrib()[1], truth['edges'])


def test_email_validation():
    truth = pd.read_csv('tests_data/q2_email.csv')
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    corrected = q.remove_rows_without_mail()
    assert truth["email"].equals(corrected["email"])


def test_fillna_rows():
    truth = np.load('tests_data/q3_fillna.npy')
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    _, rows = q.fill_na_with_mean()
    assert np.array_equal(truth, rows)
    

def test_fillna_df():
    truth = pd.read_csv('tests_data/q3_fillna.csv')
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    df, _ = q.fill_na_with_mean()
    df.equals(truth)

def test_score_exists():
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    df = q.score_subjects()
    assert "score" in df.columns


def test_score_dtype():
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    df = q.score_subjects()
    assert isinstance(df["score"].dtype, pd.UInt8Dtype)


def test_score_results():
    truth = pd.read_csv('tests_data/q4_score.csv', squeeze=True, index_col=0).astype("UInt8")
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    df = q.score_subjects()
    assert df["score"].equals(truth)


def test_correlation():
    truth = pd.read_csv('tests_data/q5_corr.csv').set_index(['gender', 'age'])
    fname = 'data.json'
    q = QuestionnaireAnalysis(fname)
    q.read_data()
    df = q.correlate_gender_age()
    pd.testing.assert_frame_equal(df, truth)
