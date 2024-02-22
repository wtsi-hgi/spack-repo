# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrcdesigns(RPackage):
	"""Generalized Row-Column Designs

	When the number of treatments is large with limited experimental resources then Row-Column(RC) designs with multiple units per cell can be used. These designs are called Generalized Row-Column (GRC) designs and are defined as designs with v treatments in p rows and q columns such that the intersection of each row and column (cell) consists of k experimental units. For example (Bailey & Monod (2001)<doi:10.1111/1467-9469.00235>), to conduct an experiment for comparing 4 treatments using 4 plants with leaves at 2 different heights row-column design with two units per cell can be used. A GRC design is said to be structurally complete if corresponding to the intersection of each row and column, there appears at least two treatments. A GRC design is said to be structurally incomplete if corresponding to the intersection of any row and column, there is at least one cell which does not contain any treatment.
	"""
	
	cran = "GRCdesigns" 

	version("1.0.0", md5="371eff28c7dec7c00812f011db1ef71b")

