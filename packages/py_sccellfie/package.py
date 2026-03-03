# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySccellfie(PythonPackage):
    """A tool for studying metabolic tasks from single-cell and spatial transcriptomics"""

    homepage = "https://github.com/earmingol/scCellFie"
    pypi = "sccellfie/scCellFie-0.3.0-py3-none-any.whl"

    version(
        "0.1.0",
        sha256="2c4778abf7fa7c08b9eb4f2e9a99d92e5d25a3dd2ddeb4acc901447962f5b539",
        expand=False,
        url="https://files.pythonhosted.org/packages/35/79/b0f6f64743090caac4e8dd457706daa361f27b7bd194f5ebec90445582f7/scCellFie-0.1.0-py3-none-any.whl",
    )
    version(
        "0.1.1",
        sha256="1ad3ba57f980af131d8d2ca91063d3d02e8ca62ce17a7ef378818c695593829c",
        expand=False,
        url="https://files.pythonhosted.org/packages/26/e2/b2b74a68fbe8767b06158ba08bba3aaf6d83c30bdce7f0917a01b021443e/scCellFie-0.1.1-py3-none-any.whl",
    )
    version(
        "0.1.10",
        sha256="722b90260f94cfe3cced5d6f77f8a69a84e5c27a54f8ba2a527f631a9d972833",
        expand=False,
        url="https://files.pythonhosted.org/packages/99/59/7bbc2e95388b4b2fa97cedb6da5c1e3c0545a706c895202c028d0da1b46a/scCellFie-0.1.10-py3-none-any.whl",
    )
    version(
        "0.1.11",
        sha256="26238cecae53e294808fe86eb0933528ec264005c4f88872bb42df0d75c1ca4a",
        expand=False,
        url="https://files.pythonhosted.org/packages/53/e9/e3e97ffe2dbb7de2f3d7968d738982a3f23c5d4a58c48a4b3f8e4315cb0e/scCellFie-0.1.11-py3-none-any.whl",
    )
    version(
        "0.1.12",
        sha256="8a77094185b2c00b4ca8f47d6cc84ec9fc250a0833f0a3e52300623e8501d839",
        expand=False,
        url="https://files.pythonhosted.org/packages/fc/d5/70109d69ea5300d5115c3afb016e370bfe3ead4c94a113c6d70ac9afaf2c/scCellFie-0.1.12-py3-none-any.whl",
    )
    version(
        "0.1.13",
        sha256="ab33fc973dc40d8e017d8899f98020f773ce607d0d9dbe6595fec75a8c2778c5",
        expand=False,
        url="https://files.pythonhosted.org/packages/02/70/df4d86661e87167367d559b9fb11097f85966fe3ebef33527f63bf56a27d/scCellFie-0.1.13-py3-none-any.whl",
    )
    version(
        "0.1.14",
        sha256="3347278a2190f13cdd3a86ce41ad156aa0f46e2f4c2bd87fff0203df2237b63c",
        expand=False,
        url="https://files.pythonhosted.org/packages/c0/95/fdd1464bb4f567ea65ae01ca0793f2d61e1ddfbd280d26d960d106fdc664/scCellFie-0.1.14-py3-none-any.whl",
    )
    version(
        "0.1.2",
        sha256="a224920d3e9a83b925cc9575d4ad6a6130c3f39199b62f388e5e024bdfe2ded8",
        expand=False,
        url="https://files.pythonhosted.org/packages/e7/aa/8938bfb28bd1d48efcae7a7a5c15ae9ee931f01837cd43fc3402668c43f9/scCellFie-0.1.2-py3-none-any.whl",
    )
    version(
        "0.1.3",
        sha256="419ec367648eb8a35d722d8cc1cce9e5fe43ef31f320d1556d0ca001a9426990",
        expand=False,
        url="https://files.pythonhosted.org/packages/8b/c0/0e9956308e86279f23664ba8d85bc504b0bb1f0b0b9a954038ee9ab72411/scCellFie-0.1.3-py3-none-any.whl",
    )
    version(
        "0.1.4",
        sha256="81071412c0ec45b74bc564b6b1033a7b41e0e7c7fa376783f6267a9c6783e264",
        expand=False,
        url="https://files.pythonhosted.org/packages/4f/65/f4eb3b3f4d30255a696d44b29acd0e9dc89c3f0da85cd54d2c1edb084754/scCellFie-0.1.4-py3-none-any.whl",
    )
    version(
        "0.1.5",
        sha256="25c1f085ef5812493fe747d040a2f020ef0ed7ac6a523aa02a09d91011a3bdd8",
        expand=False,
        url="https://files.pythonhosted.org/packages/6c/c8/c18e850dea45f195d51563a698a06bcada2c013149c0bf1734679949e75e/scCellFie-0.1.5-py3-none-any.whl",
    )
    version(
        "0.1.6",
        sha256="c48846686d26321da6bd01eea07096e6225c35315618e22e6a01a5a995239c6d",
        expand=False,
        url="https://files.pythonhosted.org/packages/ea/5a/3cbaf6a9662d615042488f0ecc3c367a2ce8ffdf2dd2f2e2ab05ac422643/scCellFie-0.1.6-py3-none-any.whl",
    )
    version(
        "0.1.7",
        sha256="d205b41f4b082caaca562cd3cc181d99bd34d2412df2e10cd2deb38f06a26ec1",
        expand=False,
        url="https://files.pythonhosted.org/packages/a3/4e/71c6b58798044cb548b8d11f802e9299f576a4696b95d3c6b980b89c4544/scCellFie-0.1.7-py3-none-any.whl",
    )
    version(
        "0.1.8",
        sha256="99c33a7ebc8e5e5bc9fa24e03c5433bbacf2128a8663c687c43a78f2cf4d4385",
        expand=False,
        url="https://files.pythonhosted.org/packages/e5/f7/c9cb8b15fbf7f67884c2a893e5b01d902bc53b94c5fce43ef034874f547a/scCellFie-0.1.8-py3-none-any.whl",
    )
    version(
        "0.2.0",
        sha256="2b6f3373a1e1a4c1487bf306ee40cbbb5fed39a5c27b6fdb0331ca58f710ec0e",
        expand=False,
        url="https://files.pythonhosted.org/packages/ed/cc/59ab0175d893944f3f3298cd2c59e56932dbbf5787aa6e3c910809863d54/scCellFie-0.2.0-py3-none-any.whl",
    )
    version(
        "0.2.1",
        sha256="3e829e4c7bf84223f3c3775dd4031202eec11fb6e8f696dd50610d08a3df102d",
        expand=False,
        url="https://files.pythonhosted.org/packages/d4/87/910ad4616c691d56120cb4abc5ccc72370eccda8009a156f645c106101ca/scCellFie-0.2.1-py3-none-any.whl",
    )
    version(
        "0.2.2",
        sha256="96a31e7f54cefdfb6289fcd502c57af3b5692391f151b43dd413d4e7bf9a5855",
        expand=False,
        url="https://files.pythonhosted.org/packages/d7/41/fa8d57a16d8587c4cb348ec2b4764b52eb2172ea4a0bbe44705abf179c15/scCellFie-0.2.2-py3-none-any.whl",
    )
    version(
        "0.2.3",
        sha256="72650d6519a5b2027b683755151b3fe062c2e8faf98a73b19b0de9e0543c4ec9",
        expand=False,
        url="https://files.pythonhosted.org/packages/c1/34/267b4e9be97dd1606af547a7d2ed724e424dce39e26a116bf8a6cb850c48/scCellFie-0.2.3-py3-none-any.whl",
    )
    version(
        "0.3.0",
        sha256="7f12aa7bb1df84686d5c2d6a04829719de3da5c234b7d7c1040d6ec2b883670f",
        expand=False,
        url="https://files.pythonhosted.org/packages/8a/e1/a43ae485426efd7d9d49549a34e4231e73b9c25e68efbeeb8c02e8b2c272/scCellFie-0.3.0-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("py-scanpy", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-cobra", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-squidpy", type=("build", "run"))
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-geopandas", type=("build", "run"))
    depends_on("py-esda", type=("build", "run"))


# {'scanpy': ['0.1.0', '0.1.1', '0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'numpy': ['0.1.0', '0.1.1', '0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'pandas': ['0.1.0', '0.1.1', '0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'cobra': ['0.1.0', '0.1.1', '0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'tqdm': ['0.1.0', '0.1.1', '0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'scipy': ['0.1.0', '0.1.1', '0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'anndata': ['0.1.0', '0.1.1', '0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.2', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'squidpy': ['0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'networkx': ['0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'geopandas': ['0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0'], 'esda': ['0.1.10', '0.1.11', '0.1.12', '0.1.13', '0.1.14', '0.1.3', '0.1.4', '0.1.5', '0.1.6', '0.1.7', '0.1.8', '0.2.0', '0.2.1', '0.2.2', '0.2.3', '0.3.0']}
