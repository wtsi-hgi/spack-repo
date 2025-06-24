# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyModelcif(PythonPackage):
	"""Package for handling ModelCIF mmCIF and BinaryCIF files"""
	
	homepage = "https://github.com/ihmwg/python-modelcif"
	pypi = "modelcif/modelcif-1.4.tar.gz" 

	version("0.1", sha256="ec42ed32219fbb8e0892786136f18bc22a7cf8372129e08ed7077f5f943d723c")
	version("0.2", sha256="27dd9e169f971410f65aafdf30aaf0c1dcc99a0d080b2df94242dd1375176805")
	version("0.3", sha256="edd583f5f0a151ec8c3a58b1e11fde0972892b8c32c549cc5b15266f8f6bda92")
	version("0.4", sha256="50b3d3e4dc651922ac5afbbfa5c4d939bbf1f0945f127501a943a9de0632b91f")
	version("0.5", sha256="49c115edbf4044d9e77359360ad62db0a8be71347ed6b93aa254405f62120fd6")
	version("0.6", sha256="bce7e70a84a19d61e813a48ae32a123761ecaabca9634c5dd08c5c24db0be433")
	version("0.7", sha256="d6acedb2c0afb7a6964b15aa275926dd8b55c88217ae82279a1667f33f6316de")
	version("0.8", sha256="ea59529e0a92eed2e8a69e4513e46c1a97ceb8c2930d79e02b9d23f9fa4e525c")
	version("0.9", sha256="67f45ddcb9fa111be984d385167ad5cc182fc9ad5a194c523a7438dd3a140012")
	version("1.0", sha256="e8375bc502a73dcfab0b7fbdd454d67d393bbb8969981eb52199d77192a3de56")
	version("1.1", sha256="e7055c5da9b9da0c7d2358c792b61a147e1f7d5756ecbdafccfd15cd9f3b66e6")
	version("1.2", sha256="517d2a7be67c96fd56dcc3b50cf7bb0b130958c325653d9925f9a5dbfe151d78")
	version("1.3", sha256="d751f553ec225fa650a246c5739027b1b482f87a69cee406465e9b7f0b220de3")
	version("1.4", sha256="fca5c1da5eb25fff3c9cd61b618fa247569f8e90cbb64774740601155d4add6e")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-ihm", type=("build", "run"))
