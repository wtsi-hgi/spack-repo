# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClassifly(RPackage):
	"""Explore Classification Models in High Dimensions

	Given $p$-dimensional training data containing $d$ groups
    (the design space), a classification algorithm (classifier) predicts
    which group new data belongs to.  Generally the input to these
    algorithms is high dimensional, and the boundaries between groups will
    be high dimensional and perhaps curvilinear or multi-faceted. This
    package implements methods for understanding the division of space
    between the groups.
	"""
	
	homepage = "http://had.co.nz/classifly"
	cran = "classifly" 

	version("0.4.1", md5="06a91454f1f41aa265ff4a9288ea327a")

	depends_on("r-class", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
