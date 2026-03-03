# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMusicnmr(RPackage):
	"""Conversion of Nuclear Magnetic Resonance Spectra in Audio Files

	A collection of functions for converting and visualization the free induction decay of mono dimensional nuclear magnetic resonance (NMR) spectra into an audio file. It facilitates the conversion of Bruker datasets in files WAV. The sound of NMR signals could provide an alternative to the current representation of the individual metabolic fingerprint and supply equally significant information. The package includes also NMR spectra of the urine samples provided by four healthy donors. Based on Cacciatore S, Saccenti E, Piccioli M. Hypothesis: the sound of the individual metabolic phenotype? Acoustic detection of NMR experiments. OMICS. 2015;19(3):147-56. <doi:10.1089/omi.2014.0131>.  
	"""
	
	cran = "musicNMR" 

	version("1.0", md5="adc4366f6fe60473b64152ba68cc87e8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
