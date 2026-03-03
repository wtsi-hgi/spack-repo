# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodexcopd(RPackage):
	"""The CODEX (Comorbidity, Obstruction, Dyspnea, and Previous
Severe Exacerbations) Index: Short and Medium-Term Prognosis in
Patients Hospitalized for Chronic Obstructive Pulmonary Disease
(COPD) Exacerbations

	Predicts 3 to 12 months prognosis in Chronic Obstructive Pulmonary Disease (COPD) patients hospitalized for severe exacerbations, as described in Almagro et al. (2014) <doi:10.1378/chest.13-1328>.
	"""
	
	cran = "codexcopd" 

	version("0.1.0", md5="02f8cd16239fe04d47fae057ff19c71d")

