from spack.package import *


class PyAePocketminer(PythonPackage):
    """AE-PocketMiner predicts cryptic binding pockets and allosteric coupling
    from a single protein structure using an attention-enabled GVP-GNN."""

    homepage = "https://github.com/bowman-lab/ae-pocketminer"
    git = "https://github.com/bowman-lab/ae-pocketminer.git"

    license("MIT")

    version("20260709", commit="3328ca0376d3e4959545bac35e036435d582ff2e")

    depends_on("python@3.10:3.11", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.26:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pandas@2.2:", type=("build", "run"))
    depends_on("py-mdtraj@1.10:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-biopython@1.84:", type=("build", "run"))
    depends_on("py-tensorflow@2.10:", type=("build", "run"))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.libexec)
        install_tree("src", prefix.libexec.src)
        install_tree("models", prefix.libexec.models)
        install("README.md", prefix.doc)
        python = spec["python"].command.path

        for script in [
            "xtal_predict.py",
            "write_bfactor_pdb.py",
            "find_key_attention_residues.py",
            "train_xtal_predictor.py",
            "train_fpocket_drug_score_labels.py",
        ]:
            filter_file(
                "from models import MQAModel",
                "import sys; sys.path.insert(0, '{0}'); from models import MQAModel".format(prefix.libexec.src),
                join_path(prefix.libexec.src, script),
                string=True,
            )
            filter_file(
                "from util import load_checkpoint",
                "import sys; sys.path.insert(0, '{0}'); from util import load_checkpoint".format(prefix.libexec.src),
                join_path(prefix.libexec.src, script),
                string=True,
            )
            filter_file(
                "from datasets import *",
                "import sys; sys.path.insert(0, '{0}'); from datasets import *".format(prefix.libexec.src),
                join_path(prefix.libexec.src, script),
                string=True,
            )
            filter_file(
                "from models import *",
                "import sys; sys.path.insert(0, '{0}'); from models import *".format(prefix.libexec.src),
                join_path(prefix.libexec.src, script),
                string=True,
            )
            filter_file(
                "from util import save_checkpoint, load_checkpoint",
                "import sys; sys.path.insert(0, '{0}'); from util import save_checkpoint, load_checkpoint".format(prefix.libexec.src),
                join_path(prefix.libexec.src, script),
                string=True,
            )

        for module in ["models.py", "gvp.py", "datasets.py", "util.py"]:
            filter_file(
                "from gvp import *",
                "import sys; sys.path.insert(0, '{0}'); from gvp import *".format(prefix.libexec.src),
                join_path(prefix.libexec.src, module),
                string=True,
            )

        for script in [
            "xtal_predict",
            "write_bfactor_pdb",
            "find_key_attention_residues",
            "train_xtal_predictor",
            "train_fpocket_drug_score_labels",
        ]:
            with open(join_path(prefix.bin, script), "w", encoding="utf-8") as fh:
                fh.write("#!{0}\n".format(python))
                fh.write("import runpy, sys\n")
                fh.write("sys.path.insert(0, '{0}')\n".format(prefix.libexec.src))
                fh.write("runpy.run_path('{0}', run_name='__main__')\n".format(join_path(prefix.libexec.src, "{0}.py".format(script))))
            set_executable(join_path(prefix.bin, script))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "find_key_attention_residues"))("--help")
            Executable(join_path(self.prefix.bin, "write_bfactor_pdb"))("--help")
