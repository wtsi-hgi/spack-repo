# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStardist(PythonPackage):
    """This repository contains the Python implementation of star-convex object detection for 2D and 3D images."""

    url = "https://github.com/stardist/stardist/archive/refs/tags/0.8.5.tar.gz"

    version("0.8.5", sha256="1941021fdaef55bcb1aa8c08bd28be83ca3a52ad17879b496cdfe13f1dab1a3e")
    version("0.8.4", sha256="c18a2b40583cb6cf185a77eedd67619e591171f716dc70db38c8d187a26a02f0")
    version("0.8.3", sha256="271acab1bcde623dac61e1a01479376ee5f43fc19820a56acdff86a1aa4f93d0")
    version("0.8.2", sha256="fbab3a60fb38f48b4136c7617f782772a466d85c7e33b4c3895a639cc68314b5")
    version("0.8.1", sha256="3d1049b2a136c44c619a858de9de67ffda96d2c51d07c1fcd8a958e87cc1b7e0")
    version("0.8.0", sha256="0aa10d5ed12981f70509972f6dd5f6770e7895fd29e52b9edf70dd33c692c994")
    version("0.7.3", sha256="3c5d6adc978e20cfc54dc3065181869b0edc8c62133afd393ec1bb79da3b60f6")
    version("0.7.2", sha256="b7a7c41dd31f3721ff31ca2887718fbd2054f6768f662b7c3904068e19c22183")
    version("0.7.1", sha256="2944dc69a826bca195bf9687b69e0d361f2c09afda777b23762230d2ed81fb16")
    version("0.7.0", sha256="c8ee9d834ffbbc3029e7836d4a15ac47eaa36a1a68de0da61b0df09b43aa50df")

    depends_on("py-csbdeep@0.7.4:", type=("build", "run"))
    depends_on("py-scikit-image", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-imageio", type=("build", "run"))
