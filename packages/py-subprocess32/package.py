# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySubprocess32(PythonPackage):
	"""A backport of the subprocess module from Python 3 for use on 2.x."""
	
	homepage = "https://github.com/google/python-subprocess32"
	pypi = "subprocess32/subprocess32-3.5.4rc2.tar.gz" 

	version("3.2.5", sha256="557b966aaee99647ec2946d8932bf06e0a9bceaab3fa2aa969986b86e770d65d")
	version("3.2.5rc1", sha256="57b5bb4e734630175ff8baca1f61f6138d488960316b0ac3faf90b288f5c4e8c")
	version("3.2.6", sha256="ddf4d46ed2be2c7e7372dfd00c464cabb6b3e29ca4113d85e26f82b3d2c220f6")
	version("3.2.7", sha256="1e450a4a4c53bf197ad6402c564b9f7a53539385918ef8f12bdf430a61036590")
	version("3.5.0", sha256="a24bac119f23fac0e53a3707b5539b214350ddd4d7d49c87d5f3be297ca1607a")
	version("3.5.0rc1", sha256="2733defaf2cb24282fdc94cc9f2e0682308d4b20e4b7a6e384580410f314c9af")
	version("3.5.0rc3", sha256="8705a2f451078dfd5534789b1baea635321a5e69cf1a54d9a3375fb40a6422c8")
	version("3.5.1", sha256="18ece9f877eca0c2521ed99a40a3a14af230c71f006d00cd0b2d6a6ddd1af171")
	version("3.5.2", sha256="eb2b989cf03ffc7166339eb34f1aa26c5ace255243337b1e22dab7caa1166687")
	version("3.5.3", sha256="6bc82992316eef3ccff319b5033809801c0c3372709c5f6985299c88ac7225c3")
	version("3.5.4", sha256="eb2937c80497978d181efa1b839ec2d9622cf9600a039a79d0e108d1f9aec79d")
	version("3.5.4b1", sha256="976defc686a7178e1fc01728f2942ec2f637776ec1b07b4d8f9dabd2e6b642e4")
	version("3.5.4rc1", sha256="32be1385030974c49146153e97a4a9bd1be5669b09a5d3906bdd8d6be1e8c636")
	version("3.5.4rc2", sha256="b886c89524e9ae874abb8b21be6160c76819885c115bc0c7ccd104ef3305adbf")

	depends_on("python@2.7", type=("build", "run"))
	depends_on("py-setuptools", type="build")
