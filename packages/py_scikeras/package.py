# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikeras(PythonPackage):
	"""Scikit-Learn API wrapper for Keras."""
	
	homepage = "https://github.com/adriangb/scikeras"
	pypi = "scikeras/scikeras-0.9.0-py3-none-any.whl" 

	version("0.1.6", sha256="8b91d6b778fc2340e14fd981bf61523a1dabdce5dd77e027931f7f2139047e70", expand=False, url="https://files.pythonhosted.org/packages/60/51/e1abbaa628d5c6faa90fb8475f0987a58156cc6ee70075e8f199ad6227f6/scikeras-0.1.6-py2.py3-none-any.whl")
	version("0.1.7", sha256="eade3d32693a0569d851838f318ef5fac77eefd85e8b37beffd8eb77bf9f00c7", expand=False, url="https://files.pythonhosted.org/packages/1b/52/f5fc1a17787f4a355fee05af45584a8c4086138bb6131a6e81bd0d0b7c1e/scikeras-0.1.7-py2.py3-none-any.whl")
	version("0.1.8", sha256="47136f8a266ee749193982f2e3642531bd544b889be1684691240978e75d2a6f", expand=False, url="https://files.pythonhosted.org/packages/01/a9/e7276beeed3295bf8e40e81306efe532f9a0c224b74edc9842c21ffebc87/scikeras-0.1.8-py2.py3-none-any.whl")
	version("0.10.0", sha256="19aaea0c78ce794f0f267e73d55fa797b7c4cd7f4085e5664c0da25e0f920724", expand=False, url="https://files.pythonhosted.org/packages/ad/d9/c33648b324897ec5af4d053fd2eff803b9ccbb31e8703466114474217177/scikeras-0.10.0-py3-none-any.whl")
	version("0.11.0", sha256="e6688bfa5d5c8050d8dfa17c01cba030a1b015b9c2d01a52a1fc5fa84105593a", expand=False, url="https://files.pythonhosted.org/packages/41/6f/53606bacb79e64f30d23410e15f3034447e97a33850d5d4366abdcf7ed84/scikeras-0.11.0-py3-none-any.whl")
	version("0.12.0", sha256="2d69a4a70118f8a0ffb1b2487b25f7c668f36ab83425fdf9a3271eb02da739ab", expand=False, url="https://files.pythonhosted.org/packages/5d/fa/9c1967952e7889d698f10ba8b6af79dfaa2e05178d97a79fbd9d1b44e589/scikeras-0.12.0-py3-none-any.whl")
	version("0.13.0", sha256="beeec4536129e316f8ffa56b32cbc097fa9168f3789feb243cadb8d9a36a0084", expand=False, url="https://files.pythonhosted.org/packages/ea/09/1c02aa24daf7a003c06f629fbb69dc9ae1bda1b247d7b8981e550d752ac9/scikeras-0.13.0-py3-none-any.whl")
	version("0.2.0", sha256="e49330412122ee1ed6c01f7f6c7d05b17a8c7b5e7c45ff544fe05060c122b468", expand=False, url="https://files.pythonhosted.org/packages/2e/2f/09e647d5ffc8492c316c5a2668614df0770f1cf29b0239522e7a4f46fe7c/scikeras-0.2.0-py3-none-any.whl")
	version("0.2.1", sha256="663ab7a8ba8a5a78c36622744cb7f27bf69efb1cf392294212051814fef283ba", expand=False, url="https://files.pythonhosted.org/packages/3f/bb/f423fcc01cc51c6bc071175aadfae4bde246d33482375fe00fb0fc6e5caf/scikeras-0.2.1-py3-none-any.whl")
	version("0.3.0", sha256="e236f23f39bd024aa0df8dbbd0a8a0fd780224b2c1337599c35d4c450084ff1d", expand=False, url="https://files.pythonhosted.org/packages/7c/5f/0abc8690e066a3ee4956f3a4a598ab39ef2d7c3503aefcb0957b688d98a5/scikeras-0.3.0-py3-none-any.whl")
	version("0.3.1", sha256="0658bf661822b3b78ab8e6487dc4191ed72e0dd029cf1047a264a1fa2d88a21e", expand=False, url="https://files.pythonhosted.org/packages/0f/78/e7e19d92812dc8627fed7265a93b62a91cbed4d471ae5716e64199a31d9d/scikeras-0.3.1-py3-none-any.whl")
	version("0.3.3", sha256="e55ae6acc3a135fb0f165a7e5e2ba8626a34848b496a7509c4c41db6f2c36c0b", expand=False, url="https://files.pythonhosted.org/packages/f6/c5/c587ad9003167fa593cee860fe40a3e4139daed2dc8daad27c3b0e97eeca/scikeras-0.3.3-py3-none-any.whl")
	version("0.4.0", sha256="8c4db606724fe284eedff3fbd65e33c677336bfc91184f828c6d78d38ca3a299", expand=False, url="https://files.pythonhosted.org/packages/22/a5/f7e45122ed9d99954fe4db9e679364402f696902c9e399d40c5b210a270a/scikeras-0.4.0-py3-none-any.whl")
	version("0.4.1", sha256="e61755f29df5b23aa30b3e6ddc8889607a6dcd936cb441de6207d185b0429ab4", expand=False, url="https://files.pythonhosted.org/packages/03/0c/941921edfe0dcc062a0e25936e3765f4c6119c518757552c0534806e7018/scikeras-0.4.1-py3-none-any.whl")
	version("0.6.0", sha256="beb4b7a9b36109c5f9b3e8054cb345ec488ad9a782e16063a3d744514730c9d0", expand=False, url="https://files.pythonhosted.org/packages/3e/33/b802962ccbaa489321e09dfa53829fc7b851b64e4466815f95add96919fb/scikeras-0.6.0-py3-none-any.whl")
	version("0.6.1", sha256="8196c1c023d0a6556fa520411928453bfb59660fb767bd75d59da21f09ad0258", expand=False, url="https://files.pythonhosted.org/packages/ff/a8/53dd10608166c81325a56ee003c2ea66c5896e6af90cdd1d4f64cbf09c9b/scikeras-0.6.1-py3-none-any.whl")
	version("0.7.0", sha256="0ff1585dd934a72a807ee136ffe941a73154ab55beacbabe90899c87b0feabed", expand=False, url="https://files.pythonhosted.org/packages/88/64/57ddbdb802e20aa399daba6156595ca768e3b90ac2cb0fe817aee7298a9c/scikeras-0.7.0-py3-none-any.whl")
	version("0.8.0", sha256="b17b62a8bbb6cbb639793555f163a8249768684765cd942a19c00fe5e4356134", expand=False, url="https://files.pythonhosted.org/packages/98/95/c8606f640e2e932cf6bdcc7626ef502d528fbfbb1024a3bb214366e6c484/scikeras-0.8.0-py3-none-any.whl")
	version("0.9.0", sha256="b8ea8096c000b7be41e4cbf6342a86f6bc8643c0615bb303be98fa8974d40b4f", expand=False, url="https://files.pythonhosted.org/packages/8b/d8/d3a94851c93d58a9afbb9681e3a5a0d4c35dabc5a564d97875b38646749f/scikeras-0.9.0-py3-none-any.whl")

	depends_on("python@3.9.0:4", type=("build", "run"))
	depends_on("py-packaging", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))

# {'scikit-learn(>=0.21.0)': ['0.1.6', '0.1.7', '0.1.8'], 'tensorflow(>=2.1.0)': ['0.1.6', '0.1.7', '0.1.8'], 'grpcio(<1.50.0);python_version>="3.10"andsys_platform=="darwin"': ['0.10.0', '0.11.0'], 'importlib-metadata(>=3);python_version<"3.8"': ['0.10.0', '0.11.0', '0.12.0', '0.7.0', '0.8.0', '0.9.0'], 'packaging(>=0.21)': ['0.10.0', '0.11.0', '0.12.0', '0.9.0'], 'scikit-learn(>=1.0.0)': ['0.10.0', '0.11.0', '0.12.0', '0.6.0', '0.6.1', '0.7.0', '0.8.0', '0.9.0'], 'tensorflow(>=2.11.0);extra=="tensorflow"': ['0.10.0', '0.11.0'], 'tensorflow-cpu(>=2.11.0);extra=="tensorflow-cpu"': ['0.10.0', '0.11.0'], 'tensorflow-io-gcs-filesystem(>=0.23.1,<0.32);sys_platform=="win32"': ['0.11.0', '0.12.0'], 'tensorflow(>=2.12.0,<2.13.0);extra=="tensorflow"': ['0.12.0'], 'tensorflow-cpu(>=2.12.0,<2.13.0);extra=="tensorflow-cpu"': ['0.12.0'], 'tensorflow-metal(>=1.1.0,<2.0.0);sys_platform=="darwin"andplatform_machine=="arm64"': ['0.12.0'], 'keras(>=3.2.0)': ['0.13.0'], 'scikit-learn(>=1.4.2)': ['0.13.0'], 'tensorflow(>=2.16.1);extra=="tensorflow"orextra=="test"': ['0.13.0'], 'scikit-learn(>=0.22.0)': ['0.2.0', '0.2.1', '0.3.3', '0.4.0', '0.4.1'], 'tensorflow(>=2.2.0)': ['0.2.0', '0.2.1'], 'importlib-metadata(>=3.4.0,<4.0.0);python_version<"3.8"': ['0.3.0', '0.3.1'], 'scikit-learn(>=0.22.0,<0.23.0)': ['0.3.0', '0.3.1'], 'tensorflow(>=2.4.0,<3.0.0)': ['0.3.0', '0.3.1'], 'importlib-metadata(>=3,<4);python_version<"3.8"': ['0.3.3', '0.4.0', '0.4.1', '0.6.0', '0.6.1'], 'tensorflow(>=2.4.0)': ['0.3.3'], 'packaging(>=0.21,<22.0)': ['0.4.1', '0.6.0', '0.6.1', '0.7.0', '0.8.0'], 'tensorflow(>=2.7.0);extra=="tensorflow"': ['0.6.1', '0.7.0', '0.8.0', '0.9.0'], 'tensorflow-cpu(>=2.7.0);extra=="tensorflow-cpu"': ['0.6.1', '0.7.0', '0.8.0', '0.9.0']}