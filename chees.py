import pygame

class Chessboard:
    # Satranç tahtası boyutları
    BOARD_SIZE = 320
    BORDER_SIZE = 80
    WIDTH, HEIGHT = BOARD_SIZE + BORDER_SIZE, BOARD_SIZE + BORDER_SIZE
    # Kare boyutu
    SQUARE_SIZE = BOARD_SIZE // 8

    # Renkler
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (128, 128, 128)

    # Tahtadaki sıralama için kullanılacak değerlerin tanımlanması
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8']

    def __init__(self):
        # Pygame penceresi oluşturma
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Satranç Tahtası')

        # Tahtayı oluşturma
        self.board = self.create_board()

    # Satranç tahtası yaratma fonksiyonu
    def create_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append((i+j) % 2) # sıradaki karenin rengi
            board.append(row)
        return board

    # Tahtayı çizdirme fonksiyonu
    def draw_board(self):
        # Tahta arkaplanı
        pygame.draw.rect(self.screen, self.GREY, (0, 0, self.WIDTH, self.HEIGHT))
        # Kareler
        for i in range(8):
            for j in range(8):
                color = self.WHITE if self.board[i][j] == 0 else self.BLACK
                pygame.draw.rect(self.screen, color, (j*self.SQUARE_SIZE+self.BORDER_SIZE//2, i*self.SQUARE_SIZE+self.BORDER_SIZE//2, self.SQUARE_SIZE, self.SQUARE_SIZE))
        # Harfler
        font = pygame.font.SysFont('Arial', 24)
        for i, letter in enumerate(self.LETTERS):
            text_surface = font.render(letter, True, self.BLACK)
            self.screen.blit(text_surface, ((i+0.5)*self.SQUARE_SIZE+self.BORDER_SIZE//2-text_surface.get_width()//2, self.BORDER_SIZE//2-text_surface.get_height()//2-20))
        # Sayılar
        for i, number in enumerate(self.NUMBERS):
            text_surface = font.render(number, True, self.BLACK)
            self.screen.blit(text_surface, (self.BORDER_SIZE//2-text_surface.get_width()//2-20, (i+0.5)*self.SQUARE_SIZE+self.BORDER_SIZE//2-text_surface.get_height()//2))

    # Oyun döngüsü
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Tahtayı çizdirme
            self.draw_board()

            # Pencereyi güncelleme
            pygame.display.flip()

        # Pygame'i kapatma
        pygame.quit()

class Player:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        self.pieces=[]
    
class Piece:
    def __init__(self,name,color,position):
        self.name=name
        self.color=color
        self.position=position

board=[['K','A','F','V','Ş','F','A','K'],
       ['P','P','P','P','P','P','P','P'],
       [' ','.',' ','.',' ','.',' ','.'],
       ['.',' ','.',' ','.',' ','.',' '],
       [' ','.',' ','.',' ','.',' ','.'],
       ['.',' ','.',' ','.',' ','.',' '],
       ['p','p','p','p','p','p','p','p'],
       ['k','a','f','v','ş','f','a','k']]

white_player=Player("white","w")
white_pieces=[
    Piece("Kale","w",(0,0)),
    Piece("At","w",(0,1)),
    Piece("Fil","w",(0,2)),
    Piece("Vezir","w",(0,3)),
    Piece("Şah","w",(0,4)),
    Piece("Fil","w",(0,5)),
    Piece("At","w",(0,6)),
    Piece("Kale","w",(0,7)),
    Piece("Piyon","w",(1,0)),
    Piece("Piyon","w",(1,1)),
    Piece("Piyon","w",(1,2)),
    Piece("Piyon","w",(1,3)),
    Piece("Piyon","w",(1,4)),
    Piece("Piyon","w",(1,5)),
    Piece("Piyon","w",(1,6)),
    Piece("Piyon","w",(1,7))
]
black_player=Player("black","b")
black_pieces=[
    Piece("Kale","b",(7,0)),
    Piece("At","b",(7,1)),
    Piece("Fil","b",(7,2)),
    Piece("Vezir","b",(7,3)),
    Piece("Şah","b",(7,4)),
    Piece("Fil","b",(7,5)),
    Piece("At","b",(7,6)),
    Piece("Kale","b",(7,7)),
    Piece("Piyon","b",(6,0)),
    Piece("Piyon","b",(6,1)),
    Piece("Piyon","b",(6,2)),
    Piece("Piyon","b",(6,3)),
    Piece("Piyon","b",(6,4)),
    Piece("Piyon","b",(6,5)),
    Piece("Piyon","b",(6,6)),
    Piece("Piyon","b",(6,7))
]
class Game:
    def __init__(self):
        self.board=[['']*8 for _ in range(8)]
        self.players=[]
        self.current_player=None
        self.turn=1
        self.game_over=False
    
    def setup_game(self,player1,player2):
        self.players=[player1,player2]
        player1=white_player
        player2=black_player
        #taşları tahtaya yerleştirmek ok
        for piece in player1.pieces:
            self.board[player1.pieces.position[0]][player1.pieces.position[1]]=piece
            piece.current_row=white_pieces.position[0]
            piece.current_column=white_pieces.position[1]

        for piece in player2.pieces:
            self.board[player2.pieces.position[0]][player2.pieces.position[1]]=piece
            piece.current_row=black_pieces.position[0]
            piece.current_column=black_pieces.position[1]

    def get_pawn_moves(self, piece, row, col):
        valid_moves = []
        direction = piece.color.value * -1
        next_row = row + direction

        # mümkün hamleler
        if self.is_valid_square(next_row, col) and not self.get_piece(next_row, col):
            valid_moves.append((next_row, col))

        # iki kare hareketi kontrol
        if row == 1 + 5 * direction and not self.get_piece(next_row + direction, col):
            valid_moves.append((next_row + direction, col))

        # atak kontrol
        for c in (-1, 1):
            attack_row, attack_col = next_row, col + c
            if self.is_valid_square(attack_row, attack_col):
                attack_piece = self.get_piece(attack_row, attack_col)
                if attack_piece and attack_piece.color != piece.color:
                    valid_moves.append((attack_row, attack_col))
                elif self.en_passant_square == (attack_row, attack_col):
                    valid_moves.append((attack_row + direction, attack_col))

        # terfi etme hamlesi
        if next_row == 0 or next_row == 7:
            for promotion_piece in (Queen(piece.color), Rook(piece.color), Bishop(piece.color), Knight(piece.color)):
                valid_moves.append((next_row, col, promotion_piece))

        return valid_moves
    
    def get_rook_moves(self, piece, row, col):
        valid_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            for i in range(1, self.BOARD_SIZE):
                next_row, next_col = row + i * d[0], col + i * d[1]
                if not self.is_valid_square(next_row, next_col):
                    break
                next_piece = self.get_piece(next_row, next_col)
                if not next_piece:
                    valid_moves.append((next_row, next_col))
                elif next_piece.color != piece.color:
                    valid_moves.append((next_row, next_col))
                    break
                else:
                    break
        return valid_moves
    def get_king_moves(self, piece, row, col):
        valid_moves = []
    
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if self.is_valid_square(r, c) and not (r == row and c == col):
                    square_piece = self.get_piece(r, c)
                    if not square_piece or square_piece.color != piece.color:
                        valid_moves.append((r, c))
    
        # Şahın rok yapabilmesi için özel durumlar
        if not piece.has_moved:
            king_side_rook = self.get_piece(row, 7)
            queen_side_rook = self.get_piece(row, 0)
            if king_side_rook and king_side_rook.piece_type == "kale" and not king_side_rook.has_moved:
                empty_squares = all([not self.get_piece(row, c) for c in range(col + 1, 7)])
                if empty_squares and not self.is_square_attacked(row, col + 1, piece.color) and not self.is_square_attacked(row, col, piece.color):
                    valid_moves.append((row, col + 2))
            if queen_side_rook and queen_side_rook.piece_type == "kale" and not queen_side_rook.has_moved:
                empty_squares = all([not self.get_piece(row, c) for c in range(col - 1, 0, -1)])
                if empty_squares and not self.is_square_attacked(row, col - 1, piece.color) and not self.is_square_attacked(row, col, piece.color):
                    valid_moves.append((row, col - 2))
    
        return valid_moves   

    def get_castle_moves(self, piece, row, col):
        valid_moves = []
        if not self.is_in_check(piece.color):
            if piece.piece_type == "kale" and not piece.has_moved:
                if self.is_valid_square(row, col - 4) and not self.get_piece(row, col - 1) and not self.get_piece(row, col - 2) and not self.get_piece(row, col - 3):
                    left_rook = self.get_piece(row, col - 4)
                    if left_rook and left_rook.piece_type == "kale" and not left_rook.has_moved:
                        if not self.is_square_attacked(piece.color, row, col - 1) and not self.is_square_attacked(piece.color, row, col - 2):
                            valid_moves.append((row, col - 2))
                if self.is_valid_square(row, col + 3) and not self.get_piece(row, col + 1) and not self.get_piece(row, col + 2):
                    right_rook = self.get_piece(row, col + 3)
                    if right_rook and right_rook.piece_type == "kale" and not right_rook.has_moved:
                        if not self.is_square_attacked(piece.color, row, col + 1) and not self.is_square_attacked(piece.color, row, col + 2):
                            valid_moves.append((row, col + 2))
        return valid_moves
    
    def get_bishop_moves(self, piece, row, col):
        valid_moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for d in directions:
            for i in range(1, 8):
                next_row, next_col = row + i * d[0], col + i * d[1]

                if not self.is_valid_square(next_row, next_col):
                    break

                next_piece = self.get_piece(next_row, next_col)

                if not next_piece:
                    valid_moves.append((next_row, next_col))
                elif next_piece.color != piece.color:
                    valid_moves.append((next_row, next_col))
                    break
                else:
                    break

        return valid_moves


    def get_queen_moves(self, piece, row, col):
        valid_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
        # kale hareketleri
        for d in directions[:4]:
            for i in range(1, self.board_size):
                new_row, new_col = row + i*d[0], col + i*d[1]
                if not self.is_valid_square(new_row, new_col):
                    break
                if not self.add_valid_move(piece, new_row, new_col, valid_moves):
                    break

        # fil hareketleri
        for d in directions[4:]:
            for i in range(1, self.board_size):
                new_row, new_col = row + i*d[0], col + i*d[1]
                if not self.is_valid_square(new_row, new_col):
                    break
                if not self.add_valid_move(piece, new_row, new_col, valid_moves):
                    break
    
        return valid_moves

    def get_valid_moves(self,piece):
        valid_moves=[]
        #olası hamleleri hesapla ok

        #taşın tipini ve uygun hamleleri hesapla
        if piece.piece_type =="piyon":
            valid_moves=self.get_pawn_moves(piece,piece.row,piece.column)
        elif piece.piece_type =="kale":
            valid_moves=self.get_rook_moves(piece,piece.row,piece.column)
        elif piece.piece_type =="at":
            valid_moves=None
        elif piece.piece_type =="fil":
            valid_moves=None
        elif piece.piece_type =="vezir":
            valid_moves=None
        elif piece.piece_type =="şah":
            valid_moves=self.get_king_moves(piece,piece.row,piece.column)


        #geçerli hamleleri filtrele ok
        for move in valid_moves:
            if move[0]<0 or move[0]>7 or move[1]<0 or move[1]>7 :
                #hamle tahtanın dışında olduğu için geçersizdir
                continue
            target_piece=self.board[move[0][move[1]]]
            if target_piece is None or target_piece.color != piece.color:
                #hedef karede taş yoksa veya hedef karedeki taş, hareket eden taşın aynı renkteki taşıysa geçerlidir
                valid_moves.append(move)

        return valid_moves
    
    def make_move(self,piece,new_position):
        #taşı yeni pozisyonuna taşı ve hamle yapılabilirliğini kontrol et
        #eğer hamle yapılabilir ise taşı yeni pozisyonuna taşı,turu bitir, yeni oyuncuya geç, diğer kontrolleri yap
        #eğer hamle yapılmaz ise hata ver
        return None
    
    def is_game_over(self):
        #oyunun bitip bitmediğini kontrol et
        return self.game_over
    
    def print_board(self):
        #tahtanın mevcut durumunu ekrana bas
        for row in self.board:
            for square in row:
                if square=='':
                    print("-",end=' ')
                else:
                    print(square.name,end=' ')
            print()

if __name__ == '__main__':
    board = Chessboard()
    board.run()