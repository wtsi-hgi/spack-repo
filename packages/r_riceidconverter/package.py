# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiceidconverter(RPackage):
	"""Convert Biological ID from RAP or MSU to SYMBOL for Oryza Sativa

	Convert one biological ID to another of rice (Oryza sativa).
    Rice(Oryza sativa) has more than one form gene ID for the genome. 
    The two main gene ID for rice genome are  the RAP (The Rice Annotation Project, <https://rapdb.dna.affrc.go.jp/>, 
    and the MSU(The Rice Genome Annotation Project, <http://rice.plantbiology.msu.edu/>.
    All RAP rice gene IDs are of the form Os##g####### as explained on the website <https://rapdb.dna.affrc.go.jp/>.
    All MSU rice gene IDs are of the form LOC_Os##g##### as explained on the website <http://rice.plantbiology.msu.edu/analyses_nomenclature.shtml>.
    All SYMBOL rice gene IDs are the unique name on the NCBI(National Center for Biotechnology Information, <https://www.ncbi.nlm.nih.gov/>.
    The TRANSCRIPTID, is the transcript id of rice, are of the form Os##t#######.
    The researchers usually need to converter between various IDs. Such as converter RAP to SYMBOLS for function searching on NCBI.
    There are a lot of websites with the function for converting RAP to MSU or MSU to RA, such as 'ID Converter' <https://rapdb.dna.affrc.go.jp/tools/converter>.
    But it is difficult to convert super multiple IDs on these websites.
    The package can convert all IDs between the three IDs (RAP, MSU and SYMBOL) regardless of the number.
	"""
	
	cran = "riceidconverter" 

	version("1.1.1", md5="6e580321172b7b1e7778af7e9ef81b7a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
