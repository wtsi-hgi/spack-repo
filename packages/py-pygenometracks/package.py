# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPygenometracks(PythonPackage):
    """Command-line tool to make beautiful and reproducible genome browser snapshots"""

    homepage = "http://pygenometracks.readthedocs.io"
    pypi = "pygenometracks/pyGenomeTracks-3.8-py2.py3-none-any.whl"

    version("0.1", sha256="59c4f702857b7417d3a975ecb4dd3ddad0dc5626ca164cfe666fef76ad8406b0")
    version(
        "1.0",
        sha256="cfe18f3ffdd693c9476c66917c5daff229b037c2f946ad26df4ede606f7c3949",
        expand=False,
        url="https://files.pythonhosted.org/packages/06/4c/2efeecd65d1e849289f2b0ff1c47159773f3a80e50d518e6f422477a8a24/pyGenomeTracks-1.0-py2.py3-none-any.whl",
    )
    version(
        "2.0",
        sha256="166edff8549408e35416227404d568f071483aadf5b6f9ba4f255e0d6161893d",
        expand=False,
        url="https://files.pythonhosted.org/packages/c0/c4/b433fa88e8334fbae7b151ce3267476f768b29b1cb5ba4e33a24f32aff59/pyGenomeTracks-2.0-py2.py3-none-any.whl",
    )
    version("2.1", sha256="34c4533b29819761d1de978f6574ae58d3cf524cda7156e643ff37bc36a564f1")
    version("3.0", sha256="744809825c98414cf7a07d8a84a6b85d4e9734c6fcd342e10f3b2fb41f8d62a0")
    version(
        "3.1",
        sha256="33736a9157902963c730bfb25d6398470fc1e466a09bfde3da8e425f8dbf49b7",
        expand=False,
        url="https://files.pythonhosted.org/packages/95/eb/f670c5c2b24f139f30fdd02dbe9b42786593e14d7a0a1654dac4d978469e/pyGenomeTracks-3.1-py2.py3-none-any.whl",
    )
    version(
        "3.1.1",
        sha256="557eaf8ee3eceb393f24117be0407a6f3c6f6585c71cfa20546afe04d9917efe",
        expand=False,
        url="https://files.pythonhosted.org/packages/0a/b6/25d0db4ee9d3051aa28f8bdc7ee4993cd7bc5095f168dad00b6d5e201897/pyGenomeTracks-3.1.1-py2.py3-none-any.whl",
    )
    version(
        "3.1.2",
        sha256="26bcb64804e6e0e175fd428b53729d6d582220ce5dd288e8d503840311cc1359",
        expand=False,
        url="https://files.pythonhosted.org/packages/ec/f9/c7a21d7d74c316328eda3daaf133b53884834c25f693ddfb93a8fb86bc2d/pyGenomeTracks-3.1.2-py2.py3-none-any.whl",
    )
    version(
        "3.2",
        sha256="7a5f7b713c5fd05ed2e3db70b4e001ea97a74ebf71e326f2552be8dae1b36d00",
        expand=False,
        url="https://files.pythonhosted.org/packages/e7/09/c5a8440e71218793935e85dbc3f4a3f255ed693f1775e5f4e3e8cef586ab/pyGenomeTracks-3.2-py2.py3-none-any.whl",
    )
    version(
        "3.3",
        sha256="25779cbd2f50b761b190ec3af2bd6e2781e404bb9b1547ba3c8de691c9c62129",
        expand=False,
        url="https://files.pythonhosted.org/packages/41/76/657f74964bf0b616f9f580fc9fe67cee925ba62873bd8e33171c758aaf0e/pyGenomeTracks-3.3-py2.py3-none-any.whl",
    )
    version(
        "3.4",
        sha256="884bd78337fd7c1319680b7ed83c04f279e893128ef3959f016d4a4e78e8cdf2",
        expand=False,
        url="https://files.pythonhosted.org/packages/60/86/c55f6718544f3fd40b04f697d44e664c423f0682c462429ba41234d97051/pyGenomeTracks-3.4-py2.py3-none-any.whl",
    )
    version(
        "3.5",
        sha256="271b3794a7c67534d8666c53879a98a84b2c31290029dfc5556fbb0df0ad0bec",
        expand=False,
        url="https://files.pythonhosted.org/packages/1d/2b/d24b2ccfe44e80d31167c806beaa1fd1091aa8982aca4fcfff846058a604/pyGenomeTracks-3.5-py2.py3-none-any.whl",
    )
    version(
        "3.5.1",
        sha256="91c00641200b5d430a2371321b0400615d2e99de1b2a1f915519ee76a78b8f00",
        expand=False,
        url="https://files.pythonhosted.org/packages/83/96/f1e3ee7dfd6db820d6820d168e0cbf6f1049b6e7daa95e0150ca95cd468f/pyGenomeTracks-3.5.1-py2.py3-none-any.whl",
    )
    version(
        "3.6",
        sha256="949b90dcaefea2af590f48f3584205f20095ce76358bb075c3d4eebad1ecb15d",
        expand=False,
        url="https://files.pythonhosted.org/packages/b6/d9/c2776a20d6b6708b93bcb4dbe61055f0560f93f565fd4fcb80c7fcb01926/pyGenomeTracks-3.6-py2.py3-none-any.whl",
    )
    version(
        "3.7",
        sha256="6374eef5d5b4c7a1ae7b3dbea1b61d67299e3d86f268fab472969b215b1416dc",
        expand=False,
        url="https://files.pythonhosted.org/packages/b8/4c/6e6d28fb91e3f1055b6cc6b9807f1cbe7b97b947ca117219642bedf4b4a9/pyGenomeTracks-3.7-py2.py3-none-any.whl",
    )
    version(
        "3.8",
        sha256="7fecdd4a9769c7d83cb0af6d29874a46a6f12357f5bb958d5991835e205ac094",
        expand=False,
        url="https://files.pythonhosted.org/packages/f9/fb/bf8c39e693353beb08def65a7e888052a342c3fba0f3912c4ec5201e0029/pyGenomeTracks-3.8-py2.py3-none-any.whl",
    )

    depends_on("python@3.7:4", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-gffutils", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-hicmatrix", type=("build", "run"))
    depends_on("py-future", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-intervaltree", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))


# {'configparser(>=3.5.0)': ['1.0', '2.0'], 'future(>=0.16.0)': ['1.0', '2.0'], 'intervaltree(>=2.1.0)': ['1.0', '2.0', '3.1', '3.1.1', '3.1.2', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.6', '3.7', '3.8'], 'matplotlib(>=2.0.0)': ['1.0', '2.0'], 'numpy(>=1.12.1)': ['1.0', '2.0'], 'pyBigWig(>=0.3.4)': ['1.0', '2.0', '3.1', '3.1.1', '3.1.2', '3.2'], 'pytest': ['1.0', '2.0', '3.1', '3.1.1', '3.1.2', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.6', '3.7', '3.8'], 'hicexplorer(>=1.8)': ['2.0'], 'numpy(>=1.16)': ['3.1', '3.1.1', '3.1.2', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.6', '3.7'], 'matplotlib(>=3.0)': ['3.1', '3.1.1', '3.1.2'], 'future(>=0.17.0)': ['3.1', '3.1.1', '3.1.2', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.6', '3.7', '3.8'], 'hicmatrix(>=9)': ['3.1', '3.1.1', '3.1.2', '3.2'], 'pysam(>=0.14)': ['3.1', '3.1.1', '3.1.2', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.6', '3.7', '3.8'], 'gffutils(>=0.9)': ['3.1', '3.1.1', '3.1.2', '3.2', '3.3', '3.4', '3.5', '3.5.1', '3.6', '3.7', '3.8'], 'matplotlib(==3.1.1)': ['3.2', '3.3', '3.4', '3.5', '3.5.1'], 'pyBigWig(>=0.3.16)': ['3.3', '3.4', '3.5', '3.5.1', '3.6', '3.7', '3.8'], 'hicmatrix(>=12)': ['3.3', '3.4'], 'tqdm(>=4.20)': ['3.3', '3.4', '3.5', '3.5.1', '3.6', '3.7', '3.8'], 'hicmatrix(>=13)': ['3.5'], 'pybedtools(>=0.8.1)': ['3.5', '3.5.1', '3.6', '3.7', '3.8'], 'hicmatrix(>=15)': ['3.5.1', '3.6', '3.7', '3.8'], 'matplotlib(<=3.3.2,>=3.1.1)': ['3.6'], 'matplotlib(<=3.5.1,>=3.1.1)': ['3.7'], 'bx-python(>=0.8.13)': ['3.7', '3.8'], 'pyfaidx(>=0.1.3)': ['3.7', '3.8'], 'numpy(>=1.20)': ['3.8'], 'matplotlib(<=3.6.2,>=3.1.1)': ['3.8']}
