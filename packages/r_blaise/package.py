# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlaise(RPackage):
	"""Read and Write FWF Files in the 'Blaise' Format

	Can be used to read and write a fwf with an accompanying 'Blaise' datamodel.
    Blaise is the software suite built by Statistics Netherlands (CBS). It is essentially a 
    way to write and collect surveys and perform statistical analysis on the data. It stores its data in 
    fixed width format with an accompanying metadata file, this is the Blaise format. The package automatically 
    interprets this metadata and reads the file into an R dataframe.
    When supplying a datamodel for writing, the dataframe will be automatically converted 
    to that format and checked for compatibility.
    Supports dataframes, tibbles and LaF objects.
    For more information about 'Blaise', see <https://blaise.com/products/general-information>. 
	"""
	
	cran = "blaise" 

	version("1.3.11", md5="be747fc2bbffe95a300f2a5606b9b7f8")

	depends_on("r-dplyr@0.7.2:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-tibble@1.3.3:", type=("build", "run"))
