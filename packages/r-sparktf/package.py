# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparktf(RPackage):
	"""Interface for 'TensorFlow' 'TFRecord' Files with 'Apache Spark'

	A 'sparklyr' extension that enables reading and writing 'TensorFlow'
  TFRecord files via 'Apache Spark'.
	"""
	
	cran = "sparktf" 

	version("0.1.0", md5="efdec5a55ec460ba6cabf3ce19bbbe27")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-sparklyr@1:", type=("build", "run"))
	depends_on("py-tensorflow", type=("build", "link", "run"))
