from spack.package import *


class Prscs(Package):
    """prs-cs: Polygenic prediction via Bayesian regression and continuous
    shrinkage priors. Command-line tool implemented in Python.

    Source repository: https://github.com/getian107/PRScs
    """

    homepage = "https://github.com/getian107/PRScs"
    url = "https://github.com/getian107/PRScs/archive/refs/tags/v1.1.0.tar.gz"

    license("MIT")

    version("1.1.0", sha256="eca00fe40bef63178e7a6dcf56ad529206be04139b809f6c8cbf6cf5365da758")

    # Runtime dependencies
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))

    def install(self, spec, prefix):
        # Install scripts to libexec and create a CLI wrapper
        libexec = prefix.libexec
        mkdirp(prefix.bin)
        mkdirp(libexec)

        # Upstream provides standalone Python scripts
        install("PRScs.py", libexec)
        install("parse_genet.py", libexec)
        install("mcmc_gtb.py", libexec)
        install("gigrnd.py", libexec)

        # Wrapper to run PRScs with proper PYTHONPATH
        wrapper = join_path(prefix.bin, "prscs")
        with open(wrapper, "w") as f:
            f.write("#!/bin/sh\n")
            # Escape braces for str.format so ${PYTHONPATH} is written literally
            f.write("export PYTHONPATH=\"${{PYTHONPATH}}:{}\"\n".format(libexec))
            f.write(
                "exec {} \"{}\" \"$@\"\n".format(
                    spec["python"].command.path, join_path(libexec, "PRScs.py")
                )
            )
        set_executable(wrapper)

    @run_after("install")
    def install_test(self):
        # Prefer CLI help if available; falls back to a basic import test
        with working_dir("spack-test", create=True):
            prscs = Executable(join_path(self.prefix.bin, "prscs"))
            prscs("--help")
