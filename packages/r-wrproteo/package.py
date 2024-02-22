# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrproteo(RPackage):
	"""Proteomics Data Analysis Functions

	Data analysis of proteomics experiments by mass spectrometry is supported by this collection of functions mostly dedicated to the analysis of (bottom-up) quantitative (XIC) data. 
    Fasta-formatted proteomes (eg from UniProt Consortium <doi:10.1093/nar/gky1049>) can be read with automatic parsing and multiple annotation types (like species origin, abbreviated gene names, etc) extracted. 
	Initial results from multiple software for protein (and peptide) quantitation can be imported (to a common format): 
	MaxQuant (Tyanova et al 2016 <doi:10.1038/nprot.2016.136>), Dia-NN (Demichev et al 2020 <doi:10.1038/s41592-019-0638-x>), 
	Fragpipe(da Veiga et al 2020 <doi:10.1038/s41592-020-0912-y>), MassChroq (Valot et al 2011 <doi:10.1002/pmic.201100120>), 
    OpenMS (Strauss et al 2021 <doi:10.1038/nmeth.3959>), ProteomeDiscoverer (Orsburn 2021 <doi:10.3390/proteomes9010015>), 
	Proline (Bouyssie et al 2020 <doi:10.1093/bioinformatics/btaa118>), AlphaPept (preprint Strauss et al <doi:10.1101/2021.07.23.453379>) 
	and Wombat-P (Bouyssie et al 2023 <doi:10.1021/acs.jproteome.3c00636>. 
	Meta-data provided by initial analysis software and/or in sdrf format can be integrated to the analysis. 
    Quantitative proteomics measurements frequently contain multiple NA values, due to physical absence of given peptides in some samples, limitations in sensitivity or other reasons. 
    Help is provided to inspect the data graphically to investigate the nature of NA-values via their respective replicate measurements 
	and to help/confirm the choice of NA-replacement algorithms. 
	Meta-data in sdrf-format (Perez-Riverol et al 2020 <doi:10.1021/acs.jproteome.0c00376>) or similar tabular formats can be imported and included.
	Missing values can be inspected and imputed based on the concept of NA-neighbours or other methods.
    Dedicated filtering and statistical testing using the framework of package 'limma' <doi:10.18129/B9.bioc.limma> can be run, enhanced by multiple rounds of NA-replacements to provide robustness towards rare stochastic events. 
    Multi-species samples, as frequently used in benchmark-tests (eg Navarro et al 2016 <doi:10.1038/nbt.3685>, Ramus et al 2016 <doi:10.1016/j.jprot.2015.11.011>), can be run with special options considering 
    such sub-groups during normalization and testing. Subsequently, ROC curves (Hand and Till 2001 <doi:10.1023/A:1010920819831>) can be constructed to compare multiple analysis approaches.
    As detailed example the data-set from Ramus et al 2016 <doi:10.1016/j.jprot.2015.11.011>) quantified by MaxQuant, ProteomeDiscoverer,
    and Proline is provided with a detailed analysis of heterologous spike-in proteins.     
	"""
	
	cran = "wrProteo" 

	version("1.11.0.1", md5="8758fdb5bc753af163b0fb2a51c67ccb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-wrmisc@1.14.1:", type=("build", "run"))
