# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvyplot(RPackage):
	"""Produces an IVY Plot (Similar to Dot Plot) with/without
Frequencies

	For a single variable, the IVY Plot stacks tied values in the form of leaflets. Five leaflets join to form a leaf. 
    Leaves are stacked vertically. At most twenty leaves are shown; For high frequency, each leaflet may represent more than 
    one observation with multiplicity declared in the subtitle.
	"""
	
	cran = "IVYplot" 

	version("0.1.0", md5="a5a6e0e29646e10b52124a848571701f")

	depends_on("r-plyr", type=("build", "run"))
