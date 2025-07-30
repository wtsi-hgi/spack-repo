# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyChaiLab(PythonPackage):
    """Chai Discovery tools for AI + protein research."""
    
    homepage = "None"
    pypi = "chai_lab/chai_lab-0.6.1-py3-none-any.whl" 

    version("0.0.1", sha256="335ad76ceaf9b1fe6a7c147ea3e5c28874d119e71af55fdf5b161d7792d46c5a", expand=False, url="https://files.pythonhosted.org/packages/44/9b/a3b48dffc1ccdebd97c38eef6e5ba2d07885fc3d6e4dfe191afeca879e04/chai_lab-0.0.1-py3-none-any.whl")
    version("0.1.0", sha256="0edbdc71d348d9a9c01ec189f9494975f5f5585aaa5074fc2bbf757f33dd7be2", expand=False, url="https://files.pythonhosted.org/packages/5f/3e/7dbecc591b0cc779aa67eff83d9536f59a9fc491dfcb27d73df1b1bde70f/chai_lab-0.1.0-py3-none-any.whl")
    version("0.2.0", sha256="25703fd32b5de6a34ab01c6e4419b2d3ea8b5365f944d45e520475fa68770fcd", expand=False, url="https://files.pythonhosted.org/packages/2c/4c/1ff57cc4998304b605b54008b2930ea088ab24e08a9d67d0c05b6a07a17b/chai_lab-0.2.0-py3-none-any.whl")
    version("0.2.1", sha256="031392cc3c2a117c853ae0bcb00768f9f64552108f3d4b5abca28efcaaec33ba", expand=False, url="https://files.pythonhosted.org/packages/fd/a1/ff1f7d0cbbf9f4835060d5ff638bdd027d40a41ffb3b8a62acb6301a6f82/chai_lab-0.2.1-py3-none-any.whl")
    version("0.3.0", sha256="897a3f5ec8c6ccf18daf6ac3c591da7abfd6ac92d83f5cbe6275f578d4b005e2", expand=False, url="https://files.pythonhosted.org/packages/de/eb/83f166e504c40e552a1a653156703153b37e5cd5f4ffedcfb543313494aa/chai_lab-0.3.0-py3-none-any.whl")
    version("0.3.1", sha256="5c0488f77e8c316d805dca97e54f2d07a60657b59d5bffc69208fa0235b07cdb", expand=False, url="https://files.pythonhosted.org/packages/29/5a/5f69f710dafa3df996020d179e49780e78f01ed33a5cce4192378047ffb2/chai_lab-0.3.1-py3-none-any.whl")
    version("0.4.1", sha256="0b8946221c530339e5fbcc6eda7daf2ffec44a2a74c55eb47e8667ec472e878c", expand=False, url="https://files.pythonhosted.org/packages/43/d7/ed7ece38dfe815681801845a7670bea79c06d4d2ba45dd0b69a3084b6065/chai_lab-0.4.1-py3-none-any.whl")
    version("0.4.2", sha256="10ee7e1b04d5c3a24900304654396445e8bc4d59a8e9819d686a0c2ad6ac4d6a", expand=False, url="https://files.pythonhosted.org/packages/89/1c/c0b4428c1f99c598ac9bc9a82aac4a0001c097184f645b9f2fee1eef22fd/chai_lab-0.4.2-py3-none-any.whl")
    version("0.5.0", sha256="952a56db645b7764e3f02d6b392c3a4265fea30364647f314615102aba53a97c", expand=False, url="https://files.pythonhosted.org/packages/a1/32/0ccb6d7b7b2a28e89cc2a4c24acf23cf546b0006e6257bef7641a00c455f/chai_lab-0.5.0-py3-none-any.whl")
    version("0.5.1", sha256="5392150e7f2fd502f320fdf3eeb6bfc4874a2ad45c0790c47396fc7bfdba3bbf", expand=False, url="https://files.pythonhosted.org/packages/44/6f/01a9a07b8187f7158992371aae15b4a5d123bee92d523c6a8380a38fe007/chai_lab-0.5.1-py3-none-any.whl")
    version("0.5.2", sha256="44156d5329b04c81bb2feb1aa960851beab417164dae5d2fb750d295fbe64bc9", expand=False, url="https://files.pythonhosted.org/packages/b3/d9/fd20adc49cc1be921e8e5f8b2db0b6cd1bc5b8275b42f4ab8e3507e266aa/chai_lab-0.5.2-py3-none-any.whl")
    version("0.6.0", sha256="b96fc0062242b4fedc09b5351cb3ce717a9bcaeac279e2996ec49a92d5c81136", expand=False, url="https://files.pythonhosted.org/packages/64/7a/0787824ae9bacb90678aeea36a8a304bb505e8797c9f422a6b978030f9df/chai_lab-0.6.0-py3-none-any.whl")
    version("0.6.1", sha256="b49dfffec7d6962bb1bccd24d030b01d9f097122b7e9c4007b383f56bb8e60ee", expand=False, url="https://files.pythonhosted.org/packages/29/d1/6f0e38e2cf094da160640ae985baf9a330af53a98a1360bca534bae52f58/chai_lab-0.6.1-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-jaxtyping", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-gemmi", type=("build", "run"))
    depends_on("py-antipickle", type=("build", "run"))
    depends_on("py-beartype", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-typer-slim", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-rdkit", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-modelcif", type=("build", "run"))
    depends_on("py-pandera", type=("build", "run"))
    depends_on("py-tmtools", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-fastparquet", type=("build", "run"))
    depends_on("py-attrs", type=("build", "run"))

# {'antipickle==0.2.0': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'beartype>=0.18': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'biopython==1.83': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1'], 'einops~=0.8': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'gemmi~=0.6.3': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'ipykernel~=6.27': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2'], 'jaxtyping>=0.2.25': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'mypy': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2'], 'numpy~=1.21': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'pandas-stubs': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'pandas[aws,gcp,parquet]~=2.1': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'pre-commit': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2'], 'pytest': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2'], 'rdkit==2023.9.5': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'ruff==0.6.3': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2'], 'tmtools>=0.0.3': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'torch~=2.3.1': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'tqdm~=4.66': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'transformers~=4.44': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'typer~=0.12': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'types-pyyaml': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'types-requests': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'types-tqdm': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0'], 'typing-extensions': ['0.0.1', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'matplotlib': ['0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'modelcif>=1.0': ['0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'numba>=0.59': ['0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'pandera': ['0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'biopython>=1.83': ['0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.6.0', '0.6.1'], 'rdkit~=2024.9.5': ['0.6.1'], 'torch<2.7,>=2.3.1': ['0.6.1'], 'typer-slim~=0.12': ['0.6.1']}