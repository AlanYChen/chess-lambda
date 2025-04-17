from stockfishPython import Stockfish

executable_path = "/var/task/stockfish"
fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"

stockfish = Stockfish(path=executable_path)

def lambda_handler(event, context):
    print(f"event: {event}")

    stockfish.set_fen_position(fen)
    engine_output = stockfish.get_best_move()

    print(f"engine_output = {engine_output}")

    return engine_output