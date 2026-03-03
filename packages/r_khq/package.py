# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKhq(RPackage):
	"""Methods for Calculating 'KHQ' Scores and 'KHQ5D' Utility Index
Scores

	The King's Health Questionnaire (KHQ) is a disease-specific, 
  self-administered questionnaire designed specific to assess the impact of 
  Urinary Incontinence (UI) on Quality of Life. The questionnaire was developed 
  by Kelleher and collaborators (1997) <doi:10.1111/j.1471-0528.1997.tb11006.x>. 
  It is a simple, acceptable and reliable measure to use in the clinical setting 
  and a research tool that is useful in evaluating UI treatment outcomes. 
  The KHQ five dimensions (KHQ5D) is a condition-specific preference-based 
  measure developed by Brazier and collaborators (2008) <doi:10.1177/0272989X07301820>. 
  Although not as popular as the SF6D <doi:10.1016/S0895-4356(98)00103-6> and 
  EQ-5D <https://euroqol.org/>, the KHQ5D measures health-related quality of 
  life (HRQoL) specifically for UI, not general conditions like the others 
  two instruments mentioned. The KHQ5D ca be used in the clinical and economic 
  evaluation of health care. The subject self-rates their health in terms of 
  five dimensions: Role Limitation (RL), Physical Limitations (PL), Social 
  Limitations (SL), Emotions (E), and Sleep (S). Frequently the states on these 
  five dimensions are converted to a single utility index using country specific 
  value sets, which can be used in the clinical and economic evaluation of 
  health care as well as in population health surveys. This package provides 
  methods to calculate scores for each dimension of the KHQ; converts KHQ item 
  scores to KHQ5D scores; and also calculates the utility index of the KHQ5D.
	"""
	
	homepage = "https://github.com/augustobrusaca/KHQ"
	cran = "KHQ" 

	version("0.2.0", md5="2537dddc4f8f3914624c5619b316a2d0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
