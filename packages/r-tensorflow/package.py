# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorflow(RPackage):
    """R Interface to 'TensorFlow'
    
    Interface to 'TensorFlow' <https://www.tensorflow.org/>,
  an open source software library for numerical computation using data
  flow graphs. Nodes in the graph represent mathematical operations,
  while the graph edges represent the multidimensional data arrays
  (tensors) communicated between them. The flexible architecture allows
  you to deploy computation to one or more 'CPUs' or 'GPUs' in a desktop,
  server, or mobile device with a single 'API'. 'TensorFlow' was originally
  developed by researchers and engineers working on the Google Brain Team
  within Google's Machine Intelligence research organization for the
  purposes of conducting machine learning and deep neural networks research,
  but the system is general enough to be applicable in a wide variety
  of other domains as well.
    """

    homepage = "https://cran.r-project.org/web/packages/tensorflow"
    
    cran = "tensorflow"

    # versions
    version("2.11.0", md5="6dac1a9e08dc2cd31a452c1f216c035c")
    

    # dependencies
    depends_on("r@3.1:", type=('build', 'run'))
    depends_on("r-config", type=('build', 'run'))
    depends_on("r-processx", type=('build', 'run'))
    depends_on("r-reticulate@1.24:", type=('build', 'run'))
    depends_on("r-tfruns@1.0:", type=('build', 'run'))
    depends_on("r-yaml", type=('build', 'run'))
    depends_on("r-gr-devices", type=('build', 'run'))
    depends_on("r-tfautograph@0.3.1:", type=('build', 'run'))
    
