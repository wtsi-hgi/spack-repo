# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJabAdverseReactions(RPackage):
	"""Possible Adverse Events/Reactions from the
Vaccinations/Experimental Gene Therapies

	Provides data about the possible adverse events/reactions
    resulting from being injected with a vaccine/experimental gene therapy.
    Currently, this data set only includes information from six reference
    sources. Refer to the CITATION.cff file for the complete citations of
    the reference sources. For information about vaccination$/immunization$
    hazards, visit <https://www.questionuniverse.com/rethink.html#vaccine>,
    <https://www.ecoccs.com/healing.html#vaccines>,
    <https://www.questionuniverse.com/rethink_current_crisis.html#cov_vaccin>,
    and <https://www.questionuniverse.com/vaccination.html>.
	"""
	
	homepage = "https://gitlab.com/iembry/jab.adverse.reactions"
	cran = "jab.adverse.reactions" 

	version("1.0.3", md5="74cc45c342b65004902bf8666b64c823")

	depends_on("r@3.5:", type=("build", "run"))
