# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTls(RPackage):
	"""Tools of Total Least Squares in Error-in-Variables Models

	Functions for point and interval estimation in
	     error-in-variables models via total least squares or
	     generalized total least squares method. See Golub and Van
	     Loan (1980) <doi:10.1137/0717073>, Gleser (1981)
	     <https://www.jstor.org/stable/2240867>, Ivan Markovsky
	     and Huffel (2007) <doi:10.1016/j.sigpro.2007.04.004> for
	     more information.
	"""
	
	homepage = "https://github.com/LiYanStat/tls"
	cran = "tls" 

	version("0.1.0", md5="549245ae48bf2e394efe9853de236a97")

	depends_on("r@3.2.3:", type=("build", "run"))
