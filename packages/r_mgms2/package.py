# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgms2(RPackage):
	"""'MGMS2' for Polymicrobial Samples

	A glycolipid mass spectrometry technology has the potential to accurately identify individual bacterial species from polymicrobial samples. To develop bacterial identification algorithms (e.g. machine learning) using this glycolipid technology, it is necessary to generate a large number of various in-silico polymicrobial mass spectra that are similar to real mass spectra. 'MGMS2' (Membrane Glycolipid Mass Spectrum Simulator) generates such in-silico mass spectra, considering errors in m/z (mass-to-charge ratio) and variances of intensity values, occasions of missing signature ions, and noise peaks. It estimates summary statistics of monomicrobial mass spectra for each strain or species and simulates polymicrobial glycolipid mass spectra using the summary statistics of monomicrobial mass spectra. References: Ryu, S.Y., Wendt, G.A., Chandler, C.E., Ernst, R.K. and Goodlett, D.R. (2019) <doi:10.1021/acs.analchem.9b03340> "Model-based Spectral Library Approach for Bacterial Identification via Membrane Glycolipids." Gibb, S. and Strimmer, K. (2012) <doi:10.1093/bioinformatics/bts447> "MALDIquant: a versatile R package for the analysis of mass spectrometry data."
	"""
	
	cran = "MGMS2" 

	version("1.0.2", md5="1ebaa25d2a3228ca7c98e532aeb71f4d", url="https://cran.r-project.org/src/contrib/MGMS2_1.0.2.tar.gz")

	depends_on("r-maldiquant", type=("build", "run"))
	depends_on("r-maldiquantforeign", type=("build", "run"))
