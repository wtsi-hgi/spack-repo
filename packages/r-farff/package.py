# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFarff(RPackage):
	"""A Faster 'ARFF' File Reader and Writer

	Reads and writes 'ARFF' files. 'ARFF' (Attribute-Relation
    File Format) files are like 'CSV' files, with a little bit of added
    meta information in a header and standardized NA values. They are
    quite often used for machine learning data sets and were introduced
    for the 'WEKA' machine learning 'Java' toolbox. See
    <https://waikato.github.io/weka-wiki/formats_and_processing/arff_stable/>
    for further info on 'ARFF' and for
    <http://www.cs.waikato.ac.nz/ml/weka/> for more info on 'WEKA'.
    'farff' gets rid of the 'Java' dependency that 'RWeka' enforces, and
    it is at least a faster reader (for bigger files). It uses 'readr' as
    parser back-end for the data section of the 'ARFF' file. Consistency
    with 'RWeka' is tested on 'Github' and 'Travis CI' with hundreds of
    'ARFF' files from 'OpenML'.
	"""
	
	homepage = "https://github.com/mlr-org/farff"
	cran = "farff" 

	version("1.1.1", md5="aa03765e52d476d612600c09d8389e3a")

	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-checkmate@1.8:", type=("build", "run"))
	depends_on("r-readr@1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
