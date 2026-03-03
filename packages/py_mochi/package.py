# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyMochi(PythonPackage):
    """MoCHI: Neural networks to quantify energies, energetic couplings, epistasis and allostery from deep mutational scanning data."""

    homepage = "https://github.com/wtsi-hgi/MoCHI"
    git = "https://github.com/wtsi-hgi/MoCHI.git"

    version("20251222", commit="3c4a8da11ec270eacc41dcbe259539ef0e8e7963")
    version("1.1", tag="v1.1")
    version("1.0", tag="v1.0")

    depends_on("python@3.9:", type=("build", "run"))

    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pyreadr@0.5.3:", type=("build", "run"))
    depends_on("py-torch-gpu@2.2:", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))

    depends_on("gcc")
    depends_on("freetype")

    @run_after("install")
    def bin_install(self):
        #mkdir(self.prefix.bin)
        with open(self.prefix.bin + "/run_mochi.py", "w") as f:
            f.write("#!/bin/bash\necho -e \"from pymochi import main\\nimport sys\\nsys.exit(main.main())\" | LD_LIBRARY_PATH=\"" + self.spec["gcc"].prefix.lib64 + ":" + self.spec["freetype"].prefix.lib + ":$LD_LIBRARY_PATH" + "\" python3.9 - \"$@\"")

        with open(self.prefix.bin + "/demo_mochi.py", "w") as f:
            f.write("#!/bin/bash\necho -e \"from pymochi import main\\nimport sys\\nsys.exit(main.main(demo_mode = True))\" | LD_LIBRARY_PATH=\"" + self.spec["gcc"].prefix.lib64 + ":" + self.spec["freetype"].prefix.lib + ":$LD_LIBRARY_PATH" + "\" python3.9 - \"$@\"")

        os.chmod(self.prefix.bin + "/run_mochi.py", 0o755)
        os.chmod(self.prefix.bin + "/demo_mochi.py", 0o755)

    def setup_run_environment(self, env):
        env.prepend_path("PATH", self.prefix.bin)


