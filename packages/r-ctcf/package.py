# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtcf(RPackage):
	"""Genomic coordinates of CTCF binding sites, with orientation

	Genomic coordinates of CTCF binding sites, with strand orientation (directionality of binding). Position weight matrices (PWMs) from JASPAR, HOCOMOCO, CIS-BP, CTCFBSDB, SwissRegulon, Jolma 2013, were used to uniformly predict CTCF binding sites using FIMO (default settings) on human (hg18, hg19, hg38, T2T) and mouse (mm9, mm10, mm39) genome assemblies. Extra columns include motif/PWM name (e.g., MA0139.1), score, p-value, q-value, and the motif sequence. It is recommended to filter FIMO-predicted sites by 1e-6 p-value threshold instead of using the default 1e-4 threshold. Experimentally obtained CTCF-bound cis-regulatory elements from ENCODE SCREEN and predicted CTCF sites from CTCFBSDB are also included. Selected data are lifted over from a different genome assembly as we demonstrated liftOver is a viable option to obtain CTCF coordinates in different genome assemblies. CTCF sites obtained using JASPAR's MA0139.1 PWM and filtered at 1e-6 p-value threshold are recommended.
	"""
	
	homepage = "https://github.com/dozmorovlab/CTCF"
	bioc = "CTCF" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/CTCF_0.99.11.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/CTCF/CTCF_0.99.11.tar.gz"]

	version("0.99.11", md5="5ec44245864395de390e68fa56e465af")


	# annotation