# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS2(RPackage):
	"""Spherical Geometry Operators Using the S2 Geometry Library.

	Provides R bindings for Google's s2 library for geometric calculations on
	the sphere. High-performance constructors and exporters provide high
	compatibility with existing spatial packages, transformers construct new
	geometries from existing geometries, predicates provide a means to select
	geometries based on spatial relationships, and accessors extract
	information about geometries."""

	cran = "s2"

	version("1.1.6", md5="557af6f39ceb2b616d0b84ea238a0d61", url="https://cran.r-project.org/src/contrib/s2_1.1.6.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))
	depends_on("openssl@1.0.1:", type=("build", "link", "run"))
