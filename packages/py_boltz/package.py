# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBoltz(PythonPackage):
    """Boltz is a family of models for biomolecular interaction prediction. Boltz-1 was the first fully open source model to approach AlphaFold3 accuracy. Our latest work Boltz-2 is a new biomolecular foundation model that goes beyond AlphaFold3 and Boltz-1 by jointly modeling complex structures and binding affinities, a critical component towards accurate molecular design."""
    
    homepage = "https://github.com/jwohlwend/boltz"
    pypi = "boltz/boltz-2.2.0-py3-none-any.whl" 

    version("0.0.0", sha256="98b357bf2379f5d7ec61bbeda427430a84dc5d7c9168f44256ff8550ed0eca74", expand=False, url="https://files.pythonhosted.org/packages/8c/6e/5f97fe75288798510e7fb2e9b853799c90ed10a527cebf451852a477e871/boltz-0.0.0-py3-none-any.whl")
    version("0.1.0", sha256="79d5ed642c461887acb6bb570dc8e8fd013b346677b0df4af50b59bc9db898fd", expand=False, url="https://files.pythonhosted.org/packages/d1/10/adb2a0b96e47e5d11c8385a90d74e5cf823fc033a60a30199e0c34128823/boltz-0.1.0-py3-none-any.whl")
    version("0.2.0", sha256="223b9b29f851558a91ffba0d1257fd20fee31d2dc9bd2156b56564a45a5eac0c", expand=False, url="https://files.pythonhosted.org/packages/c7/47/e0d7dcdf922127aaab63f1abff800bf56d319519758dd7daf87d73e0f4f8/boltz-0.2.0-py3-none-any.whl")
    version("0.2.1", sha256="7e3c62aec540bbdf6f8176eabbc81d7b832b9459df9c804e0c4dcf10f540cbef", expand=False, url="https://files.pythonhosted.org/packages/12/99/e64efef6f7cef00633d9a1b762b13595ebacf0ae5cab65e76c9f8cc8e949/boltz-0.2.1-py3-none-any.whl")
    version("0.3.0", sha256="148d8d49d925b093aabd48f64aabd94a724278a6dbcd4874ef01a506ed7f092e", expand=False, url="https://files.pythonhosted.org/packages/f7/49/1a598a6936bba50b51d3aced491098caeceacef67865f0639f1e3d219eed/boltz-0.3.0-py3-none-any.whl")
    version("0.3.1", sha256="be2ad62ff3a5ebfae72fab7b483b5459af97a1cdded87e5f381a10de1dc39fe7", expand=False, url="https://files.pythonhosted.org/packages/9b/d0/7964013c9e4bf509727973d0443a81192ddbedb269ea3581a611a87bfd55/boltz-0.3.1-py3-none-any.whl")
    version("0.3.2", sha256="c14cf58bc0feb2ab8f326c5804b4f0b527f50748754993b18450b2fcbad7a0af", expand=False, url="https://files.pythonhosted.org/packages/b9/fe/9f4805a016ca37313f7f70a26343a8bfda8dd3e9d18380f7e7571d3e614d/boltz-0.3.2-py3-none-any.whl")
    version("0.4.0", sha256="b147aff416cb1e7af1f8243e29ad48c3980b63a0a46f628503df3c34f40b605a", expand=False, url="https://files.pythonhosted.org/packages/0e/42/0d154517acb1c266d69a1b97233e2242b64c38bff821c4eef0582713cbbf/boltz-0.4.0-py3-none-any.whl")
    version("0.4.1", sha256="51ffc7d26d03e97b54b8e272a77ad9f58faa437560756d401e7b25fb73146da0", expand=False, url="https://files.pythonhosted.org/packages/22/b3/6bbc7aaea024d3dc13abc8e94ee32df74dd63bfc016e0f87abd20d0dcbbd/boltz-0.4.1-py3-none-any.whl")
    version("1.0.0", sha256="87101808ffe6f0d0c2b2aba64f4972f135e448c4848a03a3348af117599678c2", expand=False, url="https://files.pythonhosted.org/packages/fa/6e/86ec06912f7b93549d442f54c2cf820f324179c8530e6734dad00811ab02/boltz-1.0.0-py3-none-any.whl")
    version("2.0.0", sha256="3fa3a0756dedf810d147c62254bc68292d2b855aa2ff1eda7e6a3d54fdbd5385", expand=False, url="https://files.pythonhosted.org/packages/73/e9/6ef84f4a0ffd4d51112249bb13bca54d196a6a7e497f9ace7d3774a8d7a0/boltz-2.0.0-py3-none-any.whl")
    version("2.0.1", sha256="61ab6355c9dbc8247d06ff0699e7623f90cc0922ff4e5bb7bb831c0b73a14d2b", expand=False, url="https://files.pythonhosted.org/packages/9c/d6/4ea8176448106ab2e199bc991e25cc08a695ca1b02adfe03097981ecf84a/boltz-2.0.1-py3-none-any.whl")
    version("2.0.2", sha256="3f6a21962031e97f4e137222eff011db77ee71500425806e1d357ffadd031592", expand=False, url="https://files.pythonhosted.org/packages/8c/51/5690b0fd00581c2a1d383e42c339ad5dbe7f57176f90f2d8b4ea9cd1d658/boltz-2.0.2-py3-none-any.whl")
    version("2.0.3", sha256="5851dd10c7819d4c011534a4e5c9cc495d95e42e0e1336617a1e9e78d6c4cf12", expand=False, url="https://files.pythonhosted.org/packages/10/ce/60902bf1cde0444b690e965b25efb32c82b6029acaec3cb8ad944bfcb4df/boltz-2.0.3-py3-none-any.whl")
    version("2.1.0", sha256="f27218eda34c6924c160a2c74fc609e5478802138f8e5818725c1369d5ba3178", expand=False, url="https://files.pythonhosted.org/packages/19/8f/80974bf24d9bb148c63f811af2f72e93f0867038ec9c73cfd8fe85a13a4b/boltz-2.1.0-py3-none-any.whl")
    version("2.1.1", sha256="1d036a689ed7a9bb24ac090b36e9af746e2350df9d4ef277e420b6d6838ba0b8", expand=False, url="https://files.pythonhosted.org/packages/7a/31/dd1991c58bbd0bb4c7d213a9b5af67cfa8f6bb2cdfe6d4edbfce2c52a34c/boltz-2.1.1-py3-none-any.whl")
    version("2.2.0", sha256="c52ccc616eb138398c6235026bec32d784b40736625092dfb999c5ddb0041546", expand=False, url="https://files.pythonhosted.org/packages/7b/67/0c00994da84488aefa382ce5d94c997339bdc3495f9fdd57d4c727c90428/boltz-2.2.0-py3-none-any.whl")

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:3.13", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-hydra-core", type=("build", "run"))
    depends_on("py-pytorch-lightning", type=("build", "run"))
    depends_on("py-rdkit", type=("build", "run"))
    depends_on("py-dm-tree", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-types-requests", type=("build", "run"))
    depends_on("py-einops", type=("build", "run"))
    depends_on("py-einx", type=("build", "run"))
    depends_on("py-fairscale", type=("build", "run"))
    depends_on("py-mashumaro", type=("build", "run"))
    depends_on("py-modelcif", type=("build", "run"))
    depends_on("py-wandb", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-gemmi@0.6.5", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-chembl-structure-pipeline", type=("build", "run"))

# {'torch>=2.2': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'numpy==1.26.3': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0'], 'hydra-core==1.3.2': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'pytorch-lightning==2.4.0': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0'], 'rdkit==2024.3.6': ['0.0.0', '0.1.0'], 'dm-tree==0.1.8': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'requests==2.32.3': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'pandas==2.2.3': ['0.0.0', '0.1.0', '0.2.0', '0.2.1'], 'types-requests': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'einops==0.8.0': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'einx==0.3.0': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'fairscale==0.4.13': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'mashumaro==3.14': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'modelcif==1.2': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'wandb==0.18.7': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'click==8.1.7': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'pyyaml==6.0.2': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'biopython==1.84': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'scipy==1.13.1': ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], "ruff;extra=='lint'": ['0.0.0', '0.1.0', '0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'rdkit>=2024.3.2': ['0.2.0', '0.2.1', '0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'pandas>=2.2.2': ['0.3.0', '0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], "pytest;extra=='test'": ['0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3'], "requests;extra=='test'": ['0.3.1', '0.3.2', '0.4.0', '0.4.1', '1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'trifast>=0.1.11': ['1.0.0'], 'numba==0.61.0': ['1.0.0', '2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'numpy<2.0,>=1.26': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'pytorch-lightning==2.5.0': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'gemmi==0.6.5': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'scikit-learn==1.6.1': ['2.0.0', '2.0.1', '2.0.2', '2.0.3', '2.1.0', '2.1.1', '2.2.0'], 'chembl-structure-pipeline==1.2.2': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'trifast>=0.1.11;platform_system=="Linux"': ['2.0.0', '2.0.1', '2.0.2', '2.0.3'], 'chembl_structure_pipeline==1.2.2': ['2.1.0', '2.1.1', '2.2.0'], 'cuequivariance_ops_cu12>=0.5.0': ['2.1.0', '2.1.1'], 'cuequivariance_ops_torch_cu12>=0.5.0': ['2.1.0', '2.1.1'], 'cuequivariance_torch>=0.5.0': ['2.1.0', '2.1.1'], 'ruff;extra=="lint"': ['2.1.0', '2.1.1', '2.2.0'], 'pytest;extra=="test"': ['2.1.0', '2.1.1', '2.2.0'], 'requests;extra=="test"': ['2.1.0', '2.1.1', '2.2.0'], 'cuequivariance_ops_cu12>=0.5.0;extra=="cuda"': ['2.2.0'], 'cuequivariance_ops_torch_cu12>=0.5.0;extra=="cuda"': ['2.2.0'], 'cuequivariance_torch>=0.5.0;extra=="cuda"': ['2.2.0']}