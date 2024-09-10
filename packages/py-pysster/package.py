# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPysster(PythonPackage):
	"""a Sequence/STructure classifiER for biological sequences"""
	
	homepage = "https://github.com/budach/pysster"
	pypi = "pysster/pysster-1.2.2.tar.gz" 

	version("1.0.1", sha256="490e572a23ad7c32bab672ef283703a5cf3ace7431fac7a79f4c7b5a8aa1250e")
	version("1.1.0", sha256="f0e7c4c3e3582c8c53c5d6826b7cc07a0fb87d806d9d88ee61320fd0d2135cf9")
	version("1.1.1", sha256="3f2b2c972cade7b3f1d60872451e0de6094232c2e205ac58a6acc58a91fe5098")
	version("1.1.2", sha256="81d8ea8c6008f0ec438c843c4d9d33ed1652c93e497467dac582847c78923d1e")
	version("1.1.3", sha256="cfc8198c6cadf15a00158696bc49fe83b7ea85443c0038093f942040af1f801a")
	version("1.1.4", sha256="d24f94a5788c62dec26b0dbd795bd0c85338872888c1fd83eb8733da2c1a94b0")
	version("1.2.0", sha256="e77371978e788a324a0d5bd545c952c199ea8c8bfb8d2297d3e8668df1a076c0")
	version("1.2.1", sha256="4baa5a24c11c74d3b78825ca847aea7da079252bb6ad98840ab21a2abd079f1f")
	version("1.2.2", sha256="0f9c3b82e8afdcc1079437f53ee6f6d46229624f0ec6d45532ae48fd56d36959")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.5:", type=("build", "run"))
