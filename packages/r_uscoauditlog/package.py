# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUscoauditlog(RPackage):
	"""United States Copyright Office Product Management Division SR
Audit Data Dataset Cleaning Algorithms

	Intended to be used by the United States Copyright Office Product Management Division Business Analysts. Include algorithms for the United States Copyright Office Product Management Division SR Audit Data dataset. The algorithm takes in the SR Audit Data excel file and reformat the spreadsheet such that the values and variables fit the format of the online database. Support functions in this package include clean_str(), which cleans instances of variable AUDIT_LOG; clean_data_to_excel(), which cleans and output the reorganized SR Audit Data dataset in excel format; clean_data_to_dataframe(), which cleans and stores the reorganized SR Audit Data data set to a data frame; format_from_excel(), which reads in the outputted excel file from the clean_data_to_excel() function and formats and returns the data as a dictionary that uses FIELD types as keys and NON-FIELD types as the values of those keys. format_from_dataframe(), which reads in the outputted data frame from the clean_data_to_dataframe() function and formats and returns the data as a dictionary that uses FIELD types as keys and NON-FIELD types as the values of those keys; support_function(), which takes in the dictionary outputted either from the format_from_dataframe() or format_from_excel() function and returns the data as a formatted data frame according to the original U.S. Copyright Office SR Audit Data online database. The main function of this package is clean_format_all(), which takes in an excel file and returns the formatted data into a new excel and text file according to the format from the U.S. Copyright Office SR Audit Data online database. 
	"""
	
	cran = "uscoauditlog" 

	version("1.0.3", md5="30980f2c042d044a3e076e0db595a5ff")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
