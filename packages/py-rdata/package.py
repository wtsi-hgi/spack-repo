# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRdata(PythonPackage):
	"""Read R datasets from Python."""
	
	homepage = "https://github.com/vnmabus/rdata"
	pypi = "rdata/rdata-1.0.0-py3-none-any.whl" 

	version("0.1", sha256="5d9a6155ffb0e5ea44a50e5dd7867a625512321bf4382c2f29f9eb3292d6042c", expand=False, url="https://files.pythonhosted.org/packages/4c/9d/cc139262cca958957fc9fb4523f5658c470179652def58c79f5de1888516/rdata-0.1-py2.py3-none-any.whl")
	version("0.1.1", sha256="c5161373bf006a3cf346c9fc9cb5f758253de0872d1fff2e25917be2e6262d0f", expand=False, url="https://files.pythonhosted.org/packages/4b/ef/3bfdcde9420fb158ecbe088ab49f992534ba14e418fa638be7106db92c81/rdata-0.1.1-py2.py3-none-any.whl")
	version("0.1.2", sha256="29e3585079bb1a4a84e977e6410252d5871c6ef55a8cdaf11fca4c035f7e6a45", expand=False, url="https://files.pythonhosted.org/packages/4a/d9/da0a1337d63831541d0e443378b6d120e4012fc979b64bd8cb7dbd3a524b/rdata-0.1.2-py2.py3-none-any.whl")
	version("0.10.0", sha256="f6c8ae03b779c1449c0ff6f9fb36aaa6b17542f54b1aa2b28cfa0b5f7c679e1e", expand=False, url="https://files.pythonhosted.org/packages/3a/eb/f23c381992183f8b8b9431b56ba27e7713b47238aefd75f66cc1d0802ca1/rdata-0.10.0-py3-none-any.whl")
	version("0.11.2", sha256="d819241bcec2aaaf5d267256cbdbcbe4fcbfae66b605e7a34980049f80521450", expand=False, url="https://files.pythonhosted.org/packages/df/0b/56f33362cb4e4319e7de8dff31ea1f27517df8f4087066bc946b2272324d/rdata-0.11.2-py3-none-any.whl")
	version("0.2", sha256="89d7907567ac08949ff96892e2f100bf539aa4b60f66ef6671d3a9fd01a1def4", expand=False, url="https://files.pythonhosted.org/packages/74/97/4d1e466ef7099718802042a90ef07010b1728384c8d56e6f0183ce18d378/rdata-0.2-py2.py3-none-any.whl")
	version("0.2.1", sha256="3f211fe0f69f541245f9c39a34f848bcb728c4c53ae0cff1c095bccbbf5fca45", expand=False, url="https://files.pythonhosted.org/packages/33/04/77047e83dfc08be2702ef49315a94c925cd4119cc583092fdcaca49fcf18/rdata-0.2.1-py2.py3-none-any.whl")
	version("0.2.2", sha256="7d290ae5c95df4879a8f80a5fdf9a358232d13d78ac4215e09b8f516c7f5d53b", expand=False, url="https://files.pythonhosted.org/packages/1a/9f/78de20f86c262b87f3c397b70f2881544647d826f859cf8f16b24d824321/rdata-0.2.2-py2.py3-none-any.whl")
	version("0.2.3", sha256="a76db48e0a12ce2f1a243e38336bc402abb122d8878896f9fff74785e671fc0b", expand=False, url="https://files.pythonhosted.org/packages/97/94/f5c7cb927c823646ab54e41db8d79a0b8ac62e08fd9fa183660264466fdb/rdata-0.2.3-py2.py3-none-any.whl")
	version("0.3", sha256="3de72e2815c6d21d0caf25274a69a36c0d73a7aa0537868c189e88bea9c71524", expand=False, url="https://files.pythonhosted.org/packages/c7/8f/102c02d0c071ce10394ea5dba909ae900e906a6697d02de1761715762e35/rdata-0.3-py2.py3-none-any.whl")
	version("0.4", sha256="32ccfc8fe31f0e3f608a6ead528b15876b44a6211a2ec355f4b7af5164322950", expand=False, url="https://files.pythonhosted.org/packages/6f/a0/eae9c9c45623c636b2674a2f6d36f8d8c412c0ff731f6e23a75538ba8c9b/rdata-0.4-py2.py3-none-any.whl")
	version("0.5", sha256="e3e5817612f4a03c05ba5208d75020c7dd30e35d295c8dff26fbc9691d25d5e8", expand=False, url="https://files.pythonhosted.org/packages/5b/eb/5425f96086dff76f8de3f51f9f7c01cca472cb326ac97d1cef0f7de17270/rdata-0.5-py2.py3-none-any.whl")
	version("0.6", sha256="fe98cd248dda8deb80285f13d41c2c199b6f9a06ca596ed12be8d8fbcda0f39e", expand=False, url="https://files.pythonhosted.org/packages/22/91/d3509446e8ecaf7027b935f0cd238eef68a8f320fe7d56e5bde0b9f44dae/rdata-0.6-py2.py3-none-any.whl")
	version("0.7", sha256="ca1b4cd30296fb95caf038b0c243fd14b747da8acdbfbedac857b3240a889799", expand=False, url="https://files.pythonhosted.org/packages/66/77/80eb2166fc1dac59a624242960126d2504f2977978ef57273546263b18aa/rdata-0.7-py2.py3-none-any.whl")
	version("0.8", sha256="bc5d9dbdc606b99cd78203670d783a0bd42adfcc526d0cffdb0570dc05a4208d", expand=False, url="https://files.pythonhosted.org/packages/d6/c4/c2cb1f3db736aa4bd1e6d897eb90d79ea6c012f676530593a1cef3b7e97e/rdata-0.8-py3-none-any.whl")
	version("0.9", sha256="eec68fa652b2bbadadd81ee27f6e561b488c61d844b4a70482c160b311c5361d", expand=False, url="https://files.pythonhosted.org/packages/fc/9b/ed2b7c25bc8eb173ed8a4906e4300401c4bebcadd7ac0f456e911eef8245/rdata-0.9-py3-none-any.whl")
	version("0.9.1", sha256="c510aa4b8b1c48b43e77198cdc80c36a1f5f989a24d24e202803395158d06b22", expand=False, url="https://files.pythonhosted.org/packages/9a/01/d4170fcd7bc4302a447d57aaef0e35774fac446cb7ac9335a10a2796e00e/rdata-0.9.1-py3-none-any.whl")
	version("1.0.0", sha256="b671e31676e158dc215297595d5085aee1674b91be3c26e38638ca056167d402", expand=False, url="https://files.pythonhosted.org/packages/29/b6/aec7624eb1db90e58b7fa34ab6491ee06385020bbb9598d4b8a28051da81/rdata-1.0.0-py3-none-any.whl")

	depends_on("python@3.11:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-xarray", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-typing-extensions", type=("build", "run"))

	@run_after("install")
	def install_test(self):
		self.spec["python"].command("-c", "import rdata")
