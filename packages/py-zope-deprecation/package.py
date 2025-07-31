# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyZopeDeprecation(PythonPackage):
	"""Zope Deprecation Infrastructure"""
	
	homepage = "https://github.com/zopefoundation/zope.deprecation"
	pypi = "zope.deprecation/zope.deprecation-5.1-py3-none-any.whl" 

	version("3.3.0", sha256="86d9f7896fc301968c02d30b7663560b4d6d5a9334d697538d7a3b943a949bb4")
	version("3.4.0", sha256="010d7b72fc8cb722a6e0481863881bb6f47c2c6e75f0f0dbc4ed8f4bc6611220")
	version("3.4.1", sha256="1a4df823ae1cce7222bd7e89ba5ae9b5391d488fdc114353a4178642665acc4c")
	version("3.5.0", sha256="f73dedf51efa10bea9445bffbfcccbba1bd85ed067f9602a134c5900944caaf7")
	version("3.5.1", sha256="574330e282598a1c2601567b90ca99334c8fbb55492b280668b16ead7ffe20da")
	version("4.0.0", sha256="e07cae7d1aa12e2951efbfdcd63a2f5a74b718b028eadb495c1af41f2289febb")
	version("4.0.1", sha256="9b014aff29da33dda54a515f74e935862f90ac83fa03a4101829cd06bfb52252")
	version("4.0.2", sha256="02639fbee27bfa22f672eb18e4c173f625799459a4bc0363b86593b1d7977de6")
	version("4.1.0", sha256="c194e10775315e6f9458db77f0fd8afc97186126bf9722cc0ce77dc9731fe7ac")
	version("4.1.1", sha256="4936e2720219925b31e435e8263b9ccf56c6cdfbd078ab25604bbb0e6d2cac13")
	version("4.1.2", sha256="fed622b51ffc600c13cc5a5b6916b8514c115f34f7ea2730409f30c061eb0b78")
	version("4.2.0-py2.7", sha256="15e8a7135f40084b0e15cea9f7cb78e872b8c6a70805f0a0b91b7ce52913e31c", expand=False, url="https://files.pythonhosted.org/packages/3f/ed/83f4378b3163707de498ca1b431023018e982edbb10111aceabef3fb194e/zope.deprecation-4.2.0-py2.py3-none-any.whl")
	version("4.3.0", sha256="c83cfef3085d10dcb07de5a59a2d95713865befa46e0e88784c5648610fba789", expand=False, url="https://files.pythonhosted.org/packages/ee/33/625098914ec59b3006adf2cdf44a721e9671f4836af9eeb8cbe14e485954/zope.deprecation-4.3.0-py2.py3-none-any.whl")
	version("4.4.0", sha256="f1480b74995958b24ce37b0ef04d3663d2683e5d6debc96726eff18acf4ea113", expand=False, url="https://files.pythonhosted.org/packages/f9/26/b935bbf9d27e898b87d80e7873a0200cebf239253d0afe7a59f82fe90fff/zope.deprecation-4.4.0-py2.py3-none-any.whl")
	version("5.0", sha256="28c2ee983812efb4676d33c7a8c6ade0df191c1c6d652bbbfe6e2eeee067b2d4", expand=False, url="https://files.pythonhosted.org/packages/c8/7d/24a23d4d6d93744babfb99266eeb97a25ceae58c0f841a872b51c45ee214/zope.deprecation-5.0-py3-none-any.whl")
	version("5.1", sha256="60f957b964d8f947a4a592c647d51ce0f4f844d1f041657956ddde0d9fa9a76a", expand=False, url="https://files.pythonhosted.org/packages/30/88/5fc32633682a452260f50417da3d4be26137dd220ef617bbd8ed52f0cfa9/zope.deprecation-5.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.9:", type=("build", "run"))
	depends_on("py-setuptools", type=("build", "run"))
	depends_on("python@2..7", when="@4.2.0-py2.7", type=("build", "run"))

# {'setuptools': ['4.2.0-py2.7', '4.3.0', '4.4.0', '5.0', '5.1'], "Sphinx;extra=='docs'": ['4.2.0-py2.7', '4.3.0', '4.4.0', '5.0'], "coverage;extra=='testing'": ['4.2.0-py2.7'], "nose;extra=='testing'": ['4.2.0-py2.7'], "zope.testrunner;extra=='test'": ['4.3.0', '4.4.0', '5.0'], 'Sphinx;extra=="docs"': ['5.1'], 'zope.testrunner;extra=="test"': ['5.1']}