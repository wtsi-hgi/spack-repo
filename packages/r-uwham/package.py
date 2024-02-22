# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUwham(RPackage):
	"""Unbinned Weighted Histogram Analysis Method (UWHAM)

	A method for estimating log-normalizing constants (or free
        energies) and expectations from multiple distributions (such as
        multiple generalized ensembles).
	"""
	
	homepage = "http://www.stat.rutgers.edu/~ztan"
	cran = "UWHAM" 

	version("1.1", md5="2d86c29bf696fb4f81b3818db8f1f9d0")

	depends_on("r@2.9.1:", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
