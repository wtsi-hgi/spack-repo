# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFuncsigs(PythonPackage):
	"""Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+"""
	
	homepage = "http://funcsigs.readthedocs.org"
	pypi = "funcsigs/funcsigs-1.0.2-py2.py3-none-any.whl" 

	version("0.1", sha256="0e909110e7427ed0abc8b92525281e05aaf116cc2c921a185982edd48c1e0a6a")
	version("0.2", sha256="6896c54379cbaf8a0e14d095bc00fc0969f08f5f7908a86ddde7b15549c93916")
	version("0.3", sha256="71dcf5c28a97b2a5a5c39a45497d1c86863eb5474589a00bf7ade3cac0fdccaf")
	version("0.4", sha256="ff5ad9e2f8d9e5d1e8bbfbcf47722ab527cf0d51caeeed9da6d0f40799383fde", expand=False, url="https://files.pythonhosted.org/packages/5e/9f/025d4c92c6a1a94313cdf0813cd76f5700f8e5434fa15165090a6446ae22/funcsigs-0.4-py2.py3-none-any.whl")
	version("1.0.0", sha256="1c916dfbb4aad250f2a40e937dcff206da165fa29fa909ee1ea02243f7386019", expand=False, url="https://files.pythonhosted.org/packages/09/8d/17528625d12ca90651dd1f7958fd0d32b23b15f2197023372669fd683321/funcsigs-1.0.0-py2.py3-none-any.whl")
	version("1.0.1", sha256="2edd42db946babc214077be3626e1c496561daeb6e752e482d8d733a0d578f01", expand=False, url="https://files.pythonhosted.org/packages/3c/60/4bb1cbb64a46e98b8063013d271fd3e9e20832827a4d59e343889c6a7a95/funcsigs-1.0.1-py2.py3-none-any.whl")
	version("1.0.2", sha256="330cc27ccbf7f1e992e69fef78261dc7c6569012cf397db8d3de0234e6c937ca", expand=False, url="https://files.pythonhosted.org/packages/69/cb/f5be453359271714c01b9bd06126eaf2e368f1fddfff30818754b5ac2328/funcsigs-1.0.2-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))

# {'ordereddict': ['1.0.0-py2.7'], 'ordereddict;python_version<"2.7"': ['1.0.1-py2.7', '1.0.2-py2.7']}