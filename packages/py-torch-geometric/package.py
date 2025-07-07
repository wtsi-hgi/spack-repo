# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTorchGeometric(PythonPackage):
	"""Graph Neural Network Library for PyTorch"""
	
	homepage = "https://pyg.org"
	pypi = "torch-geometric/torch_geometric-2.6.1-py3-none-any.whl" 

	version("0.1.1", sha256="49cbfbe3893560ab3e05ed330da3062a7ea72ba923d674d5b3854d9e3eef4927")
	version("0.2.0", sha256="be0e7b6e296c2cf74c5cfca79ad331fa4032feceeb3b619e25d4501ccc9379a8")
	version("0.3.0", sha256="6c1e2f9c83a2f827fc3222e54ec24b85f1ee442b548e4615b24d43d66cab03d9")
	version("0.3.1", sha256="d50178dabe3008be93d2c53d68863f5f06d2ab815147e856f728fa0486bb31f3")
	version("1.0.0", sha256="ee8874b0214b91f7bdad7b3b8eb238ba23f90fdb7d57c38e5e628131b9704fe9")
	version("1.0.1", sha256="59299a4bc4f7c0d2471a9e793d1ff4856c21b4c7f00be47cc2f26753eb7051de")
	version("1.0.2", sha256="a5087acf551b0c717f2f4b5ca90f5f3662814bb47161024556cc21e3ff81c917")
	version("1.0.3", sha256="ab0a8b852c9a711f2cc72a1fa8f7bc644e927b042b3e9b3d083af1a2e44f8df9")
	version("1.1.0", sha256="27269a59b0a3bfee1f8a3795b20a50f7784295e2bebd5ec0a6e70202b4a4ad4d")
	version("1.1.1", sha256="bb7c03046a7e8962bf493acb2687057de26d3283f6b0b2711d6850fd8940222e")
	version("1.1.2", sha256="b516afeade47a008605513fe1ce7a0b506a94cf0542b43e2ce7b28e96080113c")
	version("1.2.0", sha256="9148e9a3f00115144d90e7d9e49c540d8b3bb47bd7ed3b41b5621961a14bae37")
	version("1.2.1", sha256="161af9353e35c4b65464a19d9bbd7ada96b3f05e4f934cd847ab0ba30c982f3c")
	version("1.3.0", sha256="a37f36e7277eb76c0198ac6af4841ddf3e21038e11022388b3b2483e0e80724e")
	version("1.3.1", sha256="910ed5013955e24bb8e2c336f0e3feae3e122ea3c9913102e5ed14b1efbdf89b")
	version("1.3.2", sha256="4471cf36a7c01f2e8d8df4b69d3bf6d5f8aa182570484cd716b5920d693eb900")
	version("1.4.1", sha256="5c58e35f75b4e72fc2a50b3ba0372eec3ea7ab3b2ea2a3dac985a4a51e2bd808")
	version("1.4.2", sha256="f5b758c8e5c779d3afeed885f2ec1cb95eac4d91e4c460991f6c96bafc2053cc")
	version("1.4.3", sha256="51369ad28a632a135e7eadc649e39a714107a338ff00b8d5f62ddc9f8c3a2010")
	version("1.5.0", sha256="131359fb1539ce5c837e8eb2dce8f7abd75294ae0ce44963648cd8646cfde6e1")
	version("1.6.0", sha256="fbf43fe15421c9affc4fb361ba4db55cb9d3c64d0c29576bb58d332bf6d27fef")
	version("1.6.1", sha256="158c153bd12408dd1ac0a543fc54bc7a7bd3ee6dcff83fd50031622aa4f9259d")
	version("1.6.2", sha256="e3683ff12ba9806078f6fb3b989d24150b321567773ae1fe5d4b98985a5f9ae6")
	version("1.6.3", sha256="347f693bebcc8a621eda4867dafab91c04db5f596d7ed7ecb89b242f8ab5c6a1")
	version("1.7.0", sha256="e9737bb8315ef5c4c0d459c7e7c25ed2cf3cebc46417e6c77a6542ebc9a8fea8")
	version("1.7.1", sha256="49d4ed41297cab686cb9517c7dabd462a5afb3848d5732ea3abeb247a3c53bbb")
	version("1.7.2", sha256="a57b115cb3891c81d16960380e0bc4d842da2c96bea5ca019d6d139e6f026b31")
	version("2.0.0", sha256="ccd03645467c28c2e58fce7512c04c53df19d2d01b73e4731a16283f06f7beef")
	version("2.0.1", sha256="6ec91a407ca95959c1ca2009f6702983540ccafabc7f2553d56755ff8b393f4f")
	version("2.0.2", sha256="9f5e7fbf920dc65cad28b91f923252f54d1f1490aeb4a3ff2bec5846f429ed44")
	version("2.0.3", sha256="59c41993a0f6cc0e29efa6ca6274cc97bd6557e54bf7d3d38213933f821701c6")
	version("2.0.4", sha256="d64e4c7486fcf0c7fa82f0acbf5dd52035855469708bf89f8bc7fc607671c8b7")
	version("2.1.0.post1", sha256="32347402076ccf60fa50312825178f1e3e5ce5e7b3b3a8b2729ac699da24525d")
	version("2.2.0", sha256="fdb282451fc33270e8e0b81d9aec7b70590363227dab0b1a7cb50a91d7b98e1d")
	version("2.3.0", sha256="4b44965d1d1f12ec2656d896614c9e8de11c096c5ff0dc7661b54b498fa3f766")
	version("2.3.1", sha256="454fd0bbc128a17a4b9d15010ba9f66d48ec8cd7277991b888a7770263fa125d")
	version("2.4.0", sha256="9d8eb5eec44382f4072aa5e835450f144e9edb9d164627e532e311880b6bdad0", expand=False, url="https://files.pythonhosted.org/packages/65/4e/6f9a75548a93fedcd4514ae2de9bee1e91bade6b73252b4da32f0e42ac52/torch_geometric-2.4.0-py3-none-any.whl")
	version("2.5.0", sha256="9322fef81189d870b08b5a8b44957c768c9e0ba431a81e6bd0d7cb39fcb87de8", expand=False, url="https://files.pythonhosted.org/packages/72/33/7bb7269fc46f40b77de035c285fbb21f8943b7fba9c69e6857e5a4ef9f57/torch_geometric-2.5.0-py3-none-any.whl")
	version("2.5.1", sha256="8dcdc67a7541c1fd3d6939efa4b302029cb30301fea7bd5b4a240f95a85a4810", expand=False, url="https://files.pythonhosted.org/packages/c6/52/1230fbcdfa27a75211b0e6d40feade0bceb793ec57e5cbd5ecf460af2652/torch_geometric-2.5.1-py3-none-any.whl")
	version("2.5.2", sha256="4d0ee1d4f22ef6008dac4eaae38a7a7c3cd5956837280312c1e99f39340d21ba", expand=False, url="https://files.pythonhosted.org/packages/3b/2e/739fbb4dcda94f2861b28145e490cd5148b3b412dabff71ae24fd1bb95b8/torch_geometric-2.5.2-py3-none-any.whl")
	version("2.5.3", sha256="8277abfc12600b0e8047e0c3ea2d55cc43f08c1448e73e924de827c15d0b5f85", expand=False, url="https://files.pythonhosted.org/packages/97/f0/66ad3a5263aa16efb534aaf4e7da23ffc28c84efbbd720b0c5ec174f6242/torch_geometric-2.5.3-py3-none-any.whl")
	version("2.6.0", sha256="0c72c0195266185a5c705dca457d1838f5605e9cc1c64d7d33900cfdab1f1270", expand=False, url="https://files.pythonhosted.org/packages/fc/14/569e932645bd0d91ba792287ce9a5a910b190d76295f28f4281f13633476/torch_geometric-2.6.0-py3-none-any.whl")
	version("2.6.1", sha256="8faeb353f9655f7dbec44c5e0b44c721773bdfb279994da96b9b8b12fd30f427", expand=False, url="https://files.pythonhosted.org/packages/03/9f/157e913626c1acfb3b19ce000b1a6e4e4fb177c0bc0ea0c67ca5bd714b5a/torch_geometric-2.6.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-aiohttp", type=("build", "run"))
	depends_on("py-fsspec", type=("build", "run"))
	depends_on("py-jinja2", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-psutil", type=("build", "run"))
	depends_on("py-pyparsing", type=("build", "run"))
	depends_on("py-requests", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-torch", type=("build", "run"))

# {'tqdm': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'numpy': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'scipy': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3'], 'jinja2': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'requests': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pyparsing': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'scikit-learn': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3'], 'psutil>=5.8.0': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'protobuf<4.21;extra=="benchmark"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'wandb;extra=="benchmark"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pandas;extra=="benchmark"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'networkx;extra=="benchmark"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'matplotlib;extra=="benchmark"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'torch_geometric[test];extra=="dev"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pre-commit;extra=="dev"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'torch_geometric[graphgym,modelhub];extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'ase;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'h5py;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'numba;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3'], 'sympy;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pandas;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'captum;extra=="full"': ['2.4.0'], 'rdflib;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'trimesh;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'networkx;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'graphviz;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'tabulate;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'matplotlib;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pynndescent;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'torchmetrics;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'scikit-image;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pytorch-memlab;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pgmpy;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'opt_einsum;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'statsmodels;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'rdkit;extra=="full"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'yacs;extra=="graphgym"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'hydra-core;extra=="graphgym"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3'], 'protobuf<4.21;extra=="graphgym"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pytorch-lightning;extra=="graphgym"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3'], 'huggingface_hub;extra=="modelhub"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pytest;extra=="test"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'pytest-cov;extra=="test"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'onnx;extra=="test"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'onnxruntime;extra=="test"': ['2.4.0', '2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'fsspec': ['2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'aiohttp': ['2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'captum<0.7.0;extra=="full"': ['2.5.0', '2.5.1', '2.5.2', '2.5.3', '2.6.0', '2.6.1'], 'ipython;extra=="dev"': ['2.6.0', '2.6.1'], 'matplotlib-inline;extra=="dev"': ['2.6.0', '2.6.1'], 'scipy;extra=="full"': ['2.6.0', '2.6.1'], 'scikit-learn;extra=="full"': ['2.6.0', '2.6.1'], 'numba<0.60.0;extra=="full"': ['2.6.0', '2.6.1'], 'pytorch-lightning<2.3.0;extra=="graphgym"': ['2.6.0', '2.6.1']}