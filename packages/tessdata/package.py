# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Tessdata(Package):
    """Tesseract data files."""

    url = "https://github.com/tesseract-ocr/tessdata/archive/refs/tags/4.1.0.tar.gz"

    version("4.1.0", sha256="990fffb9b7a9b52dc9a2d053a9ef6852ca2b72bd8dfb22988b0b990a700fd3c7")
    version("4.0.0", sha256="38c637d3a1763f6c3d32e8f1d979f045668676ec5feb8ee1869ee77cedd31b08")
    version("3.04.00", sha256="5dcb37198336b6953843b461ee535df1401b41008d550fc9e43d0edabca7adb1")

    def install(self, spec, prefix):
        install_tree(".", prefix + "/tessdata")

    def setup_environment(self, env):
        env.set("TESSDATA_PREFIX", self.prefix+"/tessdata")
        
    def setup_dependent_run_environment(self, env, spec):
        self.setup_environment(env)

    def setup_dependent_build_environment(self, env, spec):
        self.setup_environment(env)
