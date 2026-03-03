# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyArrayApiCompat(PythonPackage):
	"""A wrapper around NumPy and other array libraries to make them compatible with the Array API standard"""
	
	homepage = "https://data-apis.org/array-api-compat/"
	pypi = "array-api-compat/array_api_compat-1.9.1-py3-none-any.whl" 

	version("1.12.0", sha256="a0b4795b6944a9507fde54679f9350e2ad2b1e2acf4a2408a098cdc27f890a8b", expand=False, url="https://files.pythonhosted.org/packages/e0/b1/0542e0cab6f49f151a2d7a42400f84f706fc0b64e85dc1f56708b2e9fd37/array_api_compat-1.12.0-py3-none-any.whl")
	version("1.11.2", sha256="b1d0059714a4153b3ae37c989e47b07418f727be5b22908dd3cf9d19bdc2c547", expand=False, url="https://files.pythonhosted.org/packages/9f/d8/3388c7da49f522e51ab2f919797db28782216cadc9ecc9976160302cfcd6/array_api_compat-1.11.2-py3-none-any.whl")
	version("1.11.1", sha256="cf5efc8e171a65694c8d316223edebc22161dce052e994c21a9cbb4deb3d056b", expand=False, url="https://files.pythonhosted.org/packages/b4/a3/819c6bb53506ce94b0dbf3acfc060c02e65d050f42bf6c6a4a73c25d134b/array_api_compat-1.11.1-py3-none-any.whl")
	version("1.11", sha256="a6d8d11ba6a1366f0a8a838e993542539d38b638c27b8c2ac04965d322d66544", expand=False, url="https://files.pythonhosted.org/packages/30/d8/9418a940cca1a4c743130d18c0ec3c497c5bbe2ce856a1bd915c566a6efc/array_api_compat-1.11-py3-none-any.whl")
	version("1.10.0", sha256="d9066981fbc730174861b4394f38e27928827cbf7ed5becd8b1263b507c58864", expand=False, url="https://files.pythonhosted.org/packages/72/76/633dffbd77631525921ab8d8867e33abd8bdb4ac64bfabd41e88ea910940/array_api_compat-1.10.0-py3-none-any.whl")
	version("1.9.1", sha256="41a2703a662832d21619359ddddc5c0449876871f6c01e108c335f2a9432df94", expand=False, url="https://files.pythonhosted.org/packages/13/1d/2b2d33635de5dbf5e703114c11f1129394e68be16cc4dc5ccc2021a17f7b/array_api_compat-1.9.1-py3-none-any.whl")
	version("1.9", sha256="76db63c2d2461ba0e86b920c8b087f0a1617eb14de3ec29fe6811eeecad9c5e8", expand=False, url="https://files.pythonhosted.org/packages/45/78/17985eac75d04c30f8cc375e4400e20b0787dc4a1c853a8fe9fad7932f55/array_api_compat-1.9-py3-none-any.whl")
	version("1.8", sha256="140204454086264d37263bc4afe1182b428353e94e9edcc38d17b009863c982d", expand=False, url="https://files.pythonhosted.org/packages/0f/22/8228be1d3c6d4ffcf05cd89872ce65c1317b2af98d34b9d89b247d8d49cb/array_api_compat-1.8-py3-none-any.whl")
	version("1.7.1", sha256="6974f51775972f39edbca39e08f1c2e43c51401c093a0fea5ac7159875095d8a", expand=False, url="https://files.pythonhosted.org/packages/05/ae/2f11031bb9f819f6efaaa66b720b37928fbb0087161fcbae3465ae374a18/array_api_compat-1.7.1-py3-none-any.whl")
	version("1.7", sha256="e684268086bcacab6684ee15d4afbcd14a0136a215f36f05eed1e292de9776e3", expand=False, url="https://files.pythonhosted.org/packages/ae/43/75a085f4307f87f0eb399570ed8da1cf8e9dc01c0207f29420e078736f21/array_api_compat-1.7-py3-none-any.whl")
	version("1.6", sha256="0f132e698952bcebccfa941b4fc02cbc754802474b13a564208cf6cdbffb51e1", expand=False, url="https://files.pythonhosted.org/packages/dc/05/095288918b1d6f16516834b9118958c23a1dc7414af3b52b0b5865eaa758/array_api_compat-1.6-py3-none-any.whl")
	version("1.5.1", sha256="9bf347a274439409244266351de4a9e494499a0679744999d2b2c14aa898a846", expand=False, url="https://files.pythonhosted.org/packages/c9/de/982c2a1074a80b196863c9b4146732bb71beb14483737eedc12e3d5e74a9/array_api_compat-1.5.1-py3-none-any.whl")
	version("1.5", sha256="0c241453f8728d78cf948f81d644a1b5f8c96ecf1b1b621211041ef858b62374", expand=False, url="https://files.pythonhosted.org/packages/62/c6/ae856141503493501e19e0da7e5c4180fb208f47c5a7cdcccb942a1c0485/array_api_compat-1.5-py3-none-any.whl")
	version("1.4.1", sha256="dd212f0ed925763e1c3e98d822b80cb57c35ace6692a452430bb2d533e938069", expand=False, url="https://files.pythonhosted.org/packages/b8/b7/604e908c9081e901f56186184bbb52ed4eeb3bfad6d02d3d630b076c8aa5/array_api_compat-1.4.1-py3-none-any.whl")
	version("1.4", sha256="326383f5423716922724199988084250ca41074c7938bed6f9cea95d8d70f833", expand=False, url="https://files.pythonhosted.org/packages/10/cf/040c1b046fd43c02d230295e93969c7d100a4c34f4b1ccfaffdf98ef4530/array_api_compat-1.4-py3-none-any.whl")
	version("1.3", sha256="8697665824e815c7203aed4af5728c9b84793a8c44b5250ea8456bcb90bb8804", expand=False, url="https://files.pythonhosted.org/packages/b0/6a/39eaa8eb533174bcbe0f10dff25e9e054bee8b72716c0f35fc9f28356d45/array_api_compat-1.3-py3-none-any.whl")
	version("1.2", sha256="c53811dccc9960086a2c018f682e296afddcfd23657a8f10d0eba5ce9bd440e9", expand=False, url="https://files.pythonhosted.org/packages/81/59/1e8569de7418c1662b336bc27fa564bb3ced93752ed3ca764ded43b52eb5/array_api_compat-1.2-py3-none-any.whl")
	version("1.1.1", sha256="71735020e6c2d7f2b668e00968f0b6c7e0efbca459c1c85b421fd65780cb5e91", expand=False, url="https://files.pythonhosted.org/packages/c5/c2/bf3581416306fb9bdbbf2838c63844df746aad75529d94b69042420c7d9a/array_api_compat-1.1.1-py3-none-any.whl")
	version("1.1", sha256="fdbbdab8c3d0093d840671d96ba14ed90777f41c1b958e95dd6e10ec6da7943d", expand=False, url="https://files.pythonhosted.org/packages/b6/6d/c4200ca8af6c346b1c7442fadd77fdaca761b9683106fc0593177fa0f125/array_api_compat-1.1-py3-none-any.whl")
	version("1.0", sha256="b6df6f5645a0122683efb803cf0e4c9cc260b708b19054a4fadeabd9b9543734", expand=False, url="https://files.pythonhosted.org/packages/51/2b/7d5620da7ab863ac10639056301ed2f2e2bdd6c6050f82650ca02282d827/array_api_compat-1.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.10:", type=("build", "run"))