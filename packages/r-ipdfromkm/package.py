# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpdfromkm(RPackage):
	"""Map Digitized Survival Curves Back to Individual Patient Data

	
      An implementation to reconstruct individual patient data from Kaplan-Meier (K-M) survival curves, visualize and assess the accuracy of the reconstruction, then perform secondary analysis on the reconstructed data. We involve a simple function to extract the coordinates form the published K-M curves. The function is developed based on Poisot T. ’s digitize package (2011)  <doi:10.32614/RJ-2011-004> . For more complex and tangled together graphs, digitizing software, such as 'DigitizeIt' (for MAC or windows) or 'ScanIt'(for windows) can be used to get the coordinates. Additional information should also be involved to increase the accuracy, like numbers of patients at risk (often reported at 5-10 time points under the x-axis of the K-M graph), total number of patients, and total number of events. The package implements the modified iterative K-M estimation algorithm (modified-iKM) improved upon the approach proposed by Guyot (2012) <doi:10.1186/1471-2288-12-9> with some modifications. 
	"""
	
	cran = "IPDfromKM" 

	version("0.1.10", md5="98905ae8c49d917998a0bc4275eef338")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-readbitmap", type=("build", "run"))
