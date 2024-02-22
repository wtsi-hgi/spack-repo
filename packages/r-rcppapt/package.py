# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppapt(RPackage):
	"""'Rcpp' Interface to the APT Package Manager

	The 'APT Package Management System' provides Debian and
 Debian-derived Linux systems with a powerful system to resolve package
 dependencies. This package offers access directly from R.  This can
 only work on a system with a suitable 'libapt-pkg-dev' installation
 so functionality is curtailed if such a library is not found.
	"""
	
	homepage = "https://github.com/eddelbuettel/rcppapt"
	cran = "RcppAPT" 

	version("0.0.9", md5="8904a42afb7d67f19f0e89a30c1772b8")

	depends_on("r-rcpp", type=("build", "run"))
