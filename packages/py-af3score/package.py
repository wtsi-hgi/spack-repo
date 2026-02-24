# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os
from pathlib import Path


class PyAf3score(PythonPackage):
    """AF3Score provides scripting utilities and C++ extensions for evaluating
    AlphaFold3 structures."""

    homepage = "https://github.com/Mingchenchen/AF3Score"
    url = "https://github.com/Mingchenchen/AF3Score/archive/refs/tags/v2.0.0.tar.gz"

    license("CC-BY-NC-SA-4.0")

    version("2.0.0", sha256="b578ed61cb178b1e6355c8b028c23ec4e3cd51838e57fcd92d0f529c8268464c")
    version("1.0.0", sha256="16ed5242631d88b6336c811aedc04c3695d15747fd8620bb4419c3dc8fb3ba72")

    import_modules = ["alphafold3"]

    depends_on("python@3.11", type=("build", "run"))
    depends_on("py-setuptools", type=("build"))

    depends_on("cmake@3.29:", type="build")
    depends_on("ninja", type="build")
    depends_on("py-scikit-build-core@0.9:", type="build")
    depends_on("py-pybind11", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-absl-py", type=("build", "run"))
    depends_on("py-chex", type=("build", "run"))
    depends_on("py-dm-haiku", type=("build", "run"))
    depends_on("py-dm-tree", type=("build", "run"))
    depends_on("py-jax@0.4:", type=("build", "run"))
    depends_on("py-jaxlib@0.4:", type=("build", "run"))
    depends_on("py-jaxtyping", type=("build", "run"))
    depends_on("rdkit +python", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-typeguard@2.13.3:", type=("build", "run"))
    depends_on("py-zstandard", type=("build", "run"))
    depends_on("zlib", type=("build", "link"))
    depends_on("boost@1.77.0 +python +numpy cxxstd=17")


    @run_before("install")
    def install_script(self):

        def create_bin_file(file_name, old_str="", new_str=""):
            file_path = f"{self.prefix.bin}/{file_name}"

            with open(f"./{file_name}", 'r') as fh1:
                data = fh1.read()
                mkdirp(self.prefix.bin)

                if new_str and old_str:
                    data = data.replace(old_str, new_str)

                with open(f"{self.prefix.bin}/{file_name}", 'w+') as fh2:
                    fh2.write(data)

            os.chmod(file_path, 0o755)
        
        create_bin_file(
            "AF3score_pipeline.sh",
            'PYTHON_EXEC="/lustre/grp/cmclab/share/wangd/env/alphafold3/bin/python"',
            'PYTHON_EXEC=' + self.spec["python"].prefix.bin.python
        )
        create_bin_file("functions.sh")
        

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import alphafold3")
