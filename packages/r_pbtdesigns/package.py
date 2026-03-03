# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbtdesigns(RPackage):
	"""Partially Balanced t-Designs (PBtDesigns)

	The t-designs represent a generalized class of balanced incomplete block designs in which the number of blocks in which any t-tuple of treatments (t >= 2) occur together is a constant. When the focus of an experiment lies in grading and selecting treatment subgroups, t-designs would be preferred over the conventional ones, as they have the additional advantage of t-tuple balance. t-designs can be advantageously used in identifying the best crop-livestock combination for a particular location in Integrated Farming Systems that will help in generating maximum profit. But as the number of components increases, the number of possible t-component combinations will also increase. Most often, combinations derived from specific components are only practically feasible, for example, in a specific locality, farmers may not be interested in keeping a pig or goat and hence combinations involving these may not be of any use in that locality. In such situations partially balanced t-designs with few selected combinations appearing in a constant number of blocks (while others not at all appearing) may be useful (Sayantani Karmakar, Cini Varghese, Seema Jaggi & Mohd Harun (2021)<doi:10.1080/03610918.2021.2008436>). Further, every location may not have the resources to form equally sized homogeneous blocks. Partially balanced t-designs with unequal block sizes (Damaraju Raghavarao & Bei Zhou (1998)<doi:10.1080/03610929808832657>. Sayantani Karmakar, Cini Varghese, Seema Jaggi & Mohd Harun (2022)." Partially Balanced t-designs with unequal block sizes") prove to be more suitable for such situations.This package generates three series of partially balanced t-designs namely Series 1, Series 2 and Series 3. Series 1 and Series 2 are designs having equal block sizes and with treatment structures 4(t + 1) and a prime number, respectively. Series 3 consists of designs with unequal block sizes and with treatment structure n(n-1)/2. This package is based on the function named PBtD() for generating partially balanced t-designs along with their parameters, information matrices, average variance factors and canonical efficiency factors.
	"""
	
	cran = "PBtDesigns" 

	version("1.0.0", md5="dc2868231c5aadc7291d4b9352347c41")

	depends_on("r-mass", type=("build", "run"))
