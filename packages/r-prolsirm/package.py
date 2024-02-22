# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProlsirm(RPackage):
	"""Procrustes Matching for Latent Space Item Response Model

	Procrustes matching of the posterior samples of person and item latent positions from latent space item response models. The methods implemented in this package are based on work by Borg, I., Groenen, P. (1997, ISBN:978-0-387-94845-4), Jeon, M., Jin, I. H., Schweinberger, M., Baugh, S. (2021) <doi:10.1007/s11336-021-09762-5>, and Andrew, D. M., Kevin M. Q., Jong Hee Park. (2011) <doi:10.18637/jss.v042.i09>.
	"""
	
	cran = "prolsirm" 

	version("0.1.0", md5="5209d1197af1f12c9c8a57e58b0fbf47")

	depends_on("r-mcmcpack", type=("build", "run"))
