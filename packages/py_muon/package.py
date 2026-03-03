# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMuon(PythonPackage):
    """Multimodal omics analysis framework"""

    homepage = "https://github.com/scverse/muon"
    pypi = "muon/muon-0.1.7-py3-none-any.whl"

    version(
        "0.0.1",
        sha256="04d7c018424492bf25fe2584ed208b6ad7dc2eda71252e119a544adcf21e2c26",
        expand=False,
        url="https://files.pythonhosted.org/packages/c6/f0/384ad198a8c41a1993b0ca43e943ce65a6c27eea2e127eb7983636b9480d/muon-0.0.1-py3-none-any.whl",
    )
    version(
        "0.0.2",
        sha256="7f7c886d0ecfcf51f0e66fb8f1e82a3d9ff126b49cbe2f3854b58836c78da2cf",
        expand=False,
        url="https://files.pythonhosted.org/packages/f4/79/4a7f9513ece2692cce894a40b87e09eab494e85234548ae7e4f406dff70e/muon-0.0.2-py3-none-any.whl",
    )
    version(
        "0.1.0",
        sha256="b4c5fb251faf8a30199b9b768cc96a8365357a08f401c39aaba61c8adaa6cf10",
        expand=False,
        url="https://files.pythonhosted.org/packages/48/0e/80828bd193561694d6f71d063e077d8ab4c67ab69fa9ec9973c1c9a74f21/muon-0.1.0-py3-none-any.whl",
    )
    version(
        "0.1.1",
        sha256="32199244457a87a815266f2d7e1bb26db609b3cb19d90aa8f494cc17205d8aff",
        expand=False,
        url="https://files.pythonhosted.org/packages/d3/36/12d2bac07235800676a5dd1d2677cb29d035ca0ca7cc412165d9e29b45bd/muon-0.1.1-py3-none-any.whl",
    )
    version(
        "0.1.2",
        sha256="61e0290b113f85177b7596e57aa01552c07700716fac3b8267506fc8a6881dba",
        expand=False,
        url="https://files.pythonhosted.org/packages/f0/70/8ee645e08669b6bff578120d1cda4761d2644c4e4ff96e801ae59192e81b/muon-0.1.2-py3-none-any.whl",
    )
    version(
        "0.1.3",
        sha256="706266fd3e80a0427f9813a4844551776a472cea1ba0879cf68a734a9002c3fa",
        expand=False,
        url="https://files.pythonhosted.org/packages/c6/e3/08904f054742cb4841c705428d3efa07d75e91476c9922879edd81b711c4/muon-0.1.3-py3-none-any.whl",
    )
    version(
        "0.1.4",
        sha256="2477456f7e9a1d5ea48e8ab10e1ec44840b307f30c8e3e601be058f998ecf047",
        expand=False,
        url="https://files.pythonhosted.org/packages/5c/7b/10bcc7f08d810f5043a5dbcaf2f61085fac0e6efc181f2bf3ebf8d8e3e74/muon-0.1.4-py3-none-any.whl",
    )
    version(
        "0.1.5",
        sha256="16a24760514f8e0d49b2bc2f7602f0615c0fb03fcff7456b6ae093ec6a13f314",
        expand=False,
        url="https://files.pythonhosted.org/packages/8e/1a/e12b1d6a9efea45f4bb99bd6be33fff645314c6479d5fb33c5683391b015/muon-0.1.5-py3-none-any.whl",
    )
    version(
        "0.1.6",
        sha256="fa4fca136d3f446b8e9e1734ca5a9f2d02d1fcdec810d3375219d25d73269ca1",
        expand=False,
        url="https://files.pythonhosted.org/packages/35/cb/1d189382b654d433b8bf26f7c6ab4e9cea497ab35e400e96b0393041c3da/muon-0.1.6-py3-none-any.whl",
    )
    version(
        "0.1.7",
        sha256="e14387714478a6ddd4ce8584262078c469d7c90683c9e0c90ee4a4ba9484a007",
        expand=False,
        url="https://files.pythonhosted.org/packages/c0/53/06e32c4a6431efd4df0ff4465777c635809f5811e78de8d5f5f4b931f50c/muon-0.1.7-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-umap-learn", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-loompy", type=("build", "run"))
    depends_on("py-protobuf", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-mudata", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))


# {'numpy': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'pandas': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'matplotlib': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'seaborn': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'h5py': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'anndata': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'scanpy': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'sklearn': ['0.0.2', '0.1.0', '0.1.1', '0.1.2'], 'umap-learn': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'numba': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'loompy': ['0.0.2', '0.1.0', '0.1.1', '0.1.2'], 'protobuf': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'tqdm': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'sphinx>=4.0;extra=="docs"': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'sphinx-rtd-theme;extra=="docs"': ['0.0.2', '0.1.0', '0.1.1', '0.1.2'], 'readthedocs-sphinx-search;extra=="docs"': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'nbsphinx;extra=="docs"': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'sphinx_automodapi;extra=="docs"': ['0.0.2', '0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'mudata': ['0.1.1', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'pybedtools;extra=="atac"': ['0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'pysam;extra=="atac"': ['0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'scikit-learn': ['0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'pydata-sphinx-theme==0.8.1;extra=="docs"': ['0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'sphinx-book-theme==0.3.3;extra=="docs"': ['0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7'], 'pytest;extra=="test"': ['0.1.6', '0.1.7'], 'flake8;extra=="test"': ['0.1.6', '0.1.7'], 'mofapy2;extra=="test"': ['0.1.7']}
