# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQusage(RPackage):
	"""qusage: Quantitative Set Analysis for Gene Expression

	This package is an implementation the Quantitative Set Analysis for Gene Expression (QuSAGE) method described in (Yaari G. et al, Nucl Acids Res, 2013). This is a novel Gene Set Enrichment-type test, which is designed to provide a faster, more accurate, and easier to understand test for gene expression studies. qusage accounts for inter-gene correlations using the Variance Inflation Factor technique proposed by Wu et al. (Nucleic Acids Res, 2012). In addition, rather than simply evaluating the deviation from a null hypothesis with a single number (a P value), qusage quantifies gene set activity with a complete probability density function (PDF). From this PDF, P values and confidence intervals can be easily extracted. Preserving the PDF also allows for post-hoc analysis (e.g., pair-wise comparisons of gene set activity) while maintaining statistical traceability. Finally, while qusage is compatible with individual gene statistics from existing methods (e.g., LIMMA), a Welch-based method is implemented that is shown to improve specificity. The QuSAGE package also includes a mixed effects model implementation, as described in (Turner JA et al, BMC Bioinformatics, 2015), and a meta-analysis framework as described in (Meng H, et al. PLoS Comput Biol. 2019). For questions, contact Chris Bolen (cbolen1@gmail.com) or Steven Kleinstein (steven.kleinstein@yale.edu)
	"""
	
	homepage = "http://clip.med.yale.edu/qusage"
	bioc = "qusage" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/qusage_2.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/qusage/qusage_2.36.0.tar.gz"]

	version("2.36.0", sha256="bc298a26d8edd29f9263f8dcbe0933e858bfa45d6ada5c5726520cec44921ae3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-limma@3.14:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-fftw", type=("build", "run"))
