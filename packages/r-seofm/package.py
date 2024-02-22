# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeofm(RPackage):
	"""Standard Error of Measurement

	To calculate the standard error of measurement (SEM) to assess the observer variability (inter- and intra-observer variation).
    The methods used in this package are referenced from Zoran B. Popović (2017) <doi:10.21037/cdt.2017.03.12>.
	"""
	
	cran = "SEofM" 

	version("0.1.0", md5="b2c471b55a5abde0cf1aa3c1f58779ca")

	depends_on("r@3.5:", type=("build", "run"))
