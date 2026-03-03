# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpistats(RPackage):
	"""Tools for Epidemiologists

	Provides set of functions aimed at epidemiologists. 
 The package includes commands for measures of association and impact for case control studies and cohort studies. 
 It may be particularly useful for outbreak investigations including univariable analysis and stratified analysis.
 The functions for cohort studies include the CS(), CSTable() and CSInter() commands. 
 The functions for case control studies include the CC(), CCTable() and CCInter() commands. 
 References - Cornfield, J. 1956. A statistical problem arising from retrospective studies. In Vol. 4 of Proceedings of the Third Berkeley Symposium, ed. J. Neyman, 135-148. Berkeley, CA - University of California Press.
 Woolf, B. 1955. On estimating the relation between blood group disease. 
 Annals of Human Genetics 19 251-253. Reprinted in Evolution of Epidemiologic Ideas Annotated Readings on Concepts and Methods, ed. S. Greenland, pp. 108-110. 
 Newton Lower Falls, MA Epidemiology Resources.
 Gilles Desve & Peter Makary, 2007. 'CSTABLE Stata module to calculate summary table for cohort study' Statistical Software Components S456879, Boston College Department of Economics.
 Gilles Desve & Peter Makary, 2007. 'CCTABLE Stata module to calculate summary table for case-control study' Statistical Software Components S456878, Boston College Department of Economics.
	"""
	
	cran = "EpiStats" 

	version("1.6-2", md5="8bad1f5238d06fe1271eb647ee681366")

	depends_on("r-epir", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
