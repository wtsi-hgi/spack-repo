# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunspace(RPackage):
	"""Creating and Representing Functional Trait Spaces

	Estimation of functional spaces based on traits of organisms.
    The package includes functions to impute missing trait values (with or
    without considering phylogenetic information), and to create,
    represent and analyse two dimensional functional spaces based on
    principal components analysis, other ordination methods, or raw
    traits. It also allows for mapping a third variable onto the
    functional space.  See 'Carmona et al. (2021)' 
    <doi:10.1038/s41586-021-03871-y>, 'Puglielli et al.  (2021)'
    <doi:10.1111/nph.16952>, 'Carmona et al. (2021)'
    <doi:10.1126/sciadv.abf2675>, 'Carmona et al. (2019)'
    <doi:10.1002/ecy.2876> for more information.
	"""
	
	cran = "funspace" 

	version("0.2.1", md5="3e9d260db0a4b691acbc0d850e2dfc35")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-paran", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
