# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIccde(RPackage):
	"""Computation of the Double-Entry Intraclass Correlation

	The functions compute the double-entry intraclass correlation, which is an index of profile similarity (Furr, 2010; McCrae, 2008). The double-entry intraclass correlation is a more precise index of the agreement of two empirically observed profiles than the often-used intraclass correlation (McCrae, 2008). The function transforms profiles comprising correlations according to the Fisher z-transformation before the double-entry intraclass correlation is calculated. If the profiles comprise scores such as sum scores from various personality scales, it is recommended to standardize each individual score prior to computation of the double-entry intraclass correlation (McCrae, 2008). See Furr (2010) <doi:10.1080/00223890903379134> or McCrae (2008) <doi:10.1080/00223890701845104> for details.
	"""
	
	cran = "iccde" 

	version("0.3.5", md5="c41a7da6baa288bcfdbd8e0660c24922")

