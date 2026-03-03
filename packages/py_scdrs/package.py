# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-scdrs
#
# You can edit this file again by typing:
#
#     spack edit py-scdrs
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyScdrs(PythonPackage):
    """Single-cell disease relevance score (scDRS) is a method for associating 
    individual cells in single-cell RNA-seq data with disease GWASs, built on 
    top of AnnData and Scanpy."""

    homepage = "https://github.com/martinjzhang/scDRS"
    url = "https://github.com/martinjzhang/scDRS/archive/refs/tags/v1.0.2.tar.gz"

    license("MIT")

    version("1.0.2", sha256="03c83f01931c769c4c6aafd3ab7c7fe9a3496ba05083d7aa7ccc0969595ebb48")

    depends_on("python@3.5:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    
    # Dependencies from setup.py
    depends_on("py-numpy@1.19.0:", type=("build", "run"))
    depends_on("py-pandas@1.0.0:", type=("build", "run"))
    depends_on("py-scipy@1.5.0:", type=("build", "run"))
    depends_on("py-scanpy@1.6.0:", type=("build", "run"))
    depends_on("py-anndata@0.7:", type=("build", "run"))
    depends_on("py-scikit-misc@0.1.3:", type=("build", "run"))
    depends_on("py-statsmodels@0.11.0:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-fire@0.4.0:", type=("build", "run"))
    depends_on("py-pytest@6.2.0:", type=("build", "run"))

    @run_after("install")
    def set_shebang(self):
        # Create bin directory if it doesn't exist
        mkdirp(prefix.bin)
        
        # List of scripts to process
        scripts = ['compute_score.py', 'compute_downstream.py']
        
        for script in scripts:
            # Source script from package
            src = join_path(self.stage.source_path, script)
            # Destination in bin directory
            dst = join_path(self.prefix.bin, script)
            
            # Read the original script
            with open(src, 'r') as f:
                content = f.read()
            
            # Add shebang if not present
            if not content.startswith('#!/'):
                content = '#!/usr/bin/env python\n' + content
            
            # Write the modified script to bin directory
            with open(dst, 'w') as f:
                f.write(content)
            
            # Make the script executable
            chmod = which('chmod')
            chmod('+x', dst)
