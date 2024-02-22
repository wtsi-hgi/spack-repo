# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTatest(RPackage):
	"""Two-Group Ta-Test

	The ta-test is a modified two-sample or two-group t-test of Gosset (1908). In small samples with less than 15 replicates,the ta-test significantly reduces type I error rate but has almost the same power with the t-test and hence can greatly enhance reliability or reproducibility of discoveries in biology and medicine. The ta-test can test single null hypothesis or multiple null hypotheses without needing to correct p-values.
	"""
	
	cran = "tatest" 

	version("1.0", md5="339c23b77b9f090c9e54fe1322fc75cc")

	depends_on("r@3.3:", type=("build", "run"))
