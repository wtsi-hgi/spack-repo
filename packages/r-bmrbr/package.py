# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmrbr(RPackage):
	"""'BMRB' File Downloader

	Nuclear magnetic resonance (NMR) is a highly versatile analytical technique for studying molecular configuration, conformation, 
        and dynamics, especially those of biomacromolecules such as proteins. Biological Magnetic Resonance Data Bank ('BMRB') is a repository
        for Data from NMR Spectroscopy on Proteins, Peptides, Nucleic Acids, and other Biomolecules. Currently, 'BMRB' offers an R package 
        'RBMRB' to fetch data, however, it doesn't easily offer individual data file downloading and storing in a local directory. When using 
        'RBMRB', the data will stored as an R object, which fundamentally hinders the NMR researches to access the rich information from raw 
        data, for example, the metadata. Here, 'BMRBr' File Downloader ('BMRBr') offers a more fundamental, low level downloader, which will 
        download original deposited .str format file. This type of file contains information such as entry title, authors, citation, protein
        sequences, and so on.
        Many factors affect NMR experiment outputs, such as temperature, resonance sensitivity and etc., approximately 40% of the entries in the 'BMRB' have 
        chemical shift accuracy problems [1,2] Unfortunately, current reference correction methods are heavily dependent on the availability of
        assigned protein chemical shifts or protein structure. This is my current research project is going to solve, which will be included
        in the future release of the package. The current version of the package is sufficient and robust enough for downloading individual 
        'BMRB' data file from the 'BMRB' database <http://www.bmrb.wisc.edu>. The functionalities of this package includes but not limited:
        * To simplifies NMR researches by combine data downloading and results analysis together.
        * To allows NMR data reaches a broader audience that could utilize more than just chemical shifts but also metadata.
        * To offer reference corrected data for entries without assignment or structure information (future release).
        Reference:
        [1] E.L. Ulrich, H. Akutsu, J.F. Doreleijers, Y. Harano, Y.E. Ioannidis, J. Lin, et al., BioMagResBank, Nucl. Acids Res. 36 (2008) D402–8. <doi:10.1093/nar/gkm957>.
        [2] L. Wang, H.R. Eghbalnia, A. Bahrami, J.L. Markley, Linear analysis of carbon-13 chemical shift differences and its application to the detection and correction of errors in referencing and spin system identifications, J. Biomol. NMR. 32 (2005) 13–22. <doi:10.1007/s10858-005-1717-0>.
	"""
	
	homepage = "https://github.com/billchenxi/BMRBr"
	cran = "BMRBr" 

	version("0.2.0", md5="f1bf9e15242325b85afd5df799e65909")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
