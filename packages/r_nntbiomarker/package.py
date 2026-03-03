# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNntbiomarker(RPackage):
	"""Calculate Design Parameters for Biomarker Validation Studies

	Helps a clinical trial team  discuss
    the clinical goals  of a well-defined biomarker with a diagnostic,
    staging, prognostic, or predictive purpose.  From this discussion will
    come a statistical plan for a (non-randomized) validation trial.
    Both prospective and retrospective trials are supported. In a specific
    focused discussion, investigators should determine the range of
    "discomfort" for the NNT, number needed to treat.  The meaning of
    the discomfort range, [NNTlower, NNTupper], is that within this range
    most physicians would feel discomfort either in treating or withholding
    treatment. A pair of NNT values bracketing that range, NNTpos and NNTneg,
    become the targets of the study's design.  If the trial can demonstrate
    that a positive biomarker test yields an NNT less than NNTlower,
    and that a negative biomarker test yields an NNT less than NNTlower,
    then the biomarker may be useful for patients. A highlight of the package
    is visualization of a "contra-Bayes" theorem, which produces criteria for
    retrospective case-controls studies.
	"""
	
	cran = "NNTbiomarker" 

	version("0.29.11", md5="5201a4ad3bd513cc98a363251a60e32f")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvbutils", type=("build", "run"))
